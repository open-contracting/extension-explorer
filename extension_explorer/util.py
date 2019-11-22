"""
Module to keep ``views.py`` simple and high-level.
"""
import json
import os
import re
import warnings
from collections import defaultdict, OrderedDict
from copy import deepcopy
from functools import lru_cache

import json_merge_patch
import jsonpointer
import lxml.html
import requests
from commonmark import Parser, HtmlRenderer
from flask import url_for
from flask_babel import gettext
from ocdskit.schema import get_schema_fields
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify
from yaml import safe_load

OCDS_BASE_URL = 'https://standard.open-contracting.org/1.1'
LANGUAGE_CODE_SUFFIX = '_(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-(x(-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+))'  # noqa
LANGUAGE_CODE_SUFFIX_LEN = len(LANGUAGE_CODE_SUFFIX)


def commonmark(text):
    """
    Renders text as Markdown.
    """
    parser = Parser()
    ast = parser.parse(text)
    renderer = HtmlRenderer()

    # DeprecationWarning: The unescape method is deprecated and will be removed in 3.5, use html.unescape() instead.
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)

        return renderer.render(ast)


def get_extension_explorer_data_filename():
    """
    Returns the data file's path. Set it with the ``EXTENSION_EXPLORER_DATA_FILENAME`` environment variable (default:
    ``extension_explorer/data/extensions.json``).
    """
    if os.environ.get('EXTENSION_EXPLORER_DATA_FILENAME'):
        return os.environ.get('EXTENSION_EXPLORER_DATA_FILENAME')
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'extensions.json')


@lru_cache()
def get_extensions(filename=None):
    """
    Returns the data file's parsed contents.
    """
    if not filename:
        filename = get_extension_explorer_data_filename()
    with open(filename) as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def set_tags(extensions):
    """
    Adds tags and publishers to extensions, and returns profile, topic and publisher tags.
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'tags.yaml')) as f:
        data = safe_load(f)

    for extension in extensions.values():
        extension['tags'] = set()
        if extension['core'] and extension['id'] != 'milestone_documents':
            extension['tags'].add('recommended')

    groups = {}
    for prefix, tags in data.items():
        groups[prefix] = {}
        for tag in tags:
            if tag.get('hidden'):
                continue
            slug = tag['slug']
            for identifier in tag['extensions']:
                if identifier in extensions:
                    extensions[identifier]['tags'].add('{}-{}'.format(prefix, slug))
            groups[prefix][slug] = tag['title']

    publishers = {}
    for extension in extensions.values():
        latest_version = extension['latest_version']
        publisher = extension['versions'][latest_version]['publisher']
        extension['publisher'] = publisher

        slug = slugify(publisher['name'])
        extension['tags'].add('publisher-{}'.format(slug))
        publishers[slug] = publisher['name']

    return groups['profile'], groups['topic'], publishers


def get_present_and_historical_versions(extension):
    """
    Returns the present and historical versions, with release dates, in reverse chronological order.
    """
    latest_version = extension['latest_version']
    versions = extension['versions']

    historical_versions = [v for v in versions.values() if v['version'] != latest_version]
    historical_versions = sorted(historical_versions, key=lambda v: v['date'], reverse=True)
    historical_versions = [(v['version'], v['date']) for v in historical_versions]

    present_versions = [(latest_version, versions[latest_version]['date'] or gettext('latest'))]
    # For now, only the most recent frozen release is a present version.
    if latest_version == 'master' and historical_versions and historical_versions[0][1]:
        present_versions.append(historical_versions.pop(0))

    return present_versions, historical_versions


def identify_headings(html):
    """
    Adds `id` attributes to headings in the HTML, skipping any changelog sub-headings. Returns HTML and headings.
    """
    root = lxml.html.fromstring(html)

    headings = []
    slug_counts = defaultdict(int)
    previous_level = 1

    changelog_headings = ('Changelog', gettext('Changelog'))
    for element in root.iter('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        heading_level = int(element.tag[1])

        # Fix skipped heading levels.
        if heading_level > previous_level:
            heading_level = previous_level + 1

        # Skip changelog sub-headings.
        if headings and headings[-1]['text'] in changelog_headings and previous_level < heading_level:
            continue

        slug = slugify(element.text)
        if slug in slug_counts:
            heading_id = '{}-{}'.format(slug, slug_counts[slug])
        else:
            heading_id = slug
        element.attrib['id'] = heading_id

        headings.append({'id': heading_id, 'level': heading_level, 'text': element.text})
        slug_counts[slug] += 1
        previous_level = heading_level

    html = lxml.html.tostring(root).decode()

    return html, headings


def highlight_json(html):
    """
    Highlights JSON code blocks. Returns the HTML, and the CSS for highlighting.
    """
    root = lxml.html.fromstring(html)

    for code_block in root.find_class('language-json'):
        replacement = lxml.html.fromstring(highlight(code_block.text, JsonLexer(), HtmlFormatter()))
        parent = code_block.getparent()
        parent.getparent().replace(parent, replacement)

    html = lxml.html.tostring(root).decode()

    return html, HtmlFormatter().get_style_defs('.highlight')


def get_codelist_tables(extension_version, lang):
    """
    Returns a list of tables, one per codelist. Each item is a list of the codelist's name, basename, documentation URL
    (if patched), translated fieldnames, and and translated rows. Each row is a dictionary with up to three keys:
    "code", "title" and "content". The "content" value is a dictionary with "description" and "attributes" keys. The
    "description" value is the Description column value rendered from Markdown. The "attributes" value is a dictionary
    of additional column headers and values.

    The "description" value (rendered from Markdown) may contain HTML. The code supports old-style column headers like
    "Title_en" and "Description_en".
    """
    tables = []

    header_groups = (('Code',), ('Title', 'Title_en'), ('Description', 'Description_en'))
    codelist_reference_url = _ocds_codelist_reference_url(lang)
    codelist_names = _ocds_codelist_names()

    for name, codelist in extension_version['codelists'].items():
        fieldname_map = {}
        for header_group in header_groups:
            canonical_header = header_group[0]
            for header in header_group:
                try:
                    index = codelist['en']['fieldnames'].index(header)
                    fieldname_map[canonical_header] = codelist[lang]['fieldnames'][index]
                    break
                except ValueError:
                    pass

        fieldnames = list(fieldname_map.values())

        rows = []
        for row in codelist[lang]['rows']:
            new_row = {}

            if 'Code' in fieldname_map:
                new_row['code'] = row[fieldname_map['Code']]

            if 'Title' in fieldname_map:
                new_row['title'] = row[fieldname_map['Title']]

            content = {}
            if 'Description' in fieldname_map:
                content['description'] = commonmark(row[fieldname_map['Description']])

            attributes = OrderedDict([(k, v) for k, v in sorted(row.items()) if k not in fieldnames and v])
            if attributes:
                content['attributes'] = attributes

            if content:
                new_row['content'] = content
                # Add the column if the row has no description, but other attributes.
                if 'Description' not in fieldname_map:
                    fieldnames.append(gettext('Description'))

            rows.append(new_row)

        if name.startswith(('+', '-')):
            basename = name[1:]
        else:
            basename = name

        url = None
        if basename in codelist_names:
            anchor = re.sub(r'[A-Z]', lambda s: '-' + s[0].lower(), basename.replace('.csv', ''))
            url = '{}#{}'.format(codelist_reference_url, anchor)

        tables.append([name, basename, url, fieldnames, rows])

    return tables


def get_removed_fields(extension_version, lang):
    """
    Returns a dictionary of deprecation status and field tables. Each table is a list of fields. Each field is a
    dictionary with "definition_path", "path" and "url" (if available) keys. All values are translated.
    """
    tables = defaultdict(list)

    schema = _patch_schema(extension_version, 'en', include_test_dependencies=True)
    sources = _get_sources(schema, lang)

    for field in get_schema_fields(extension_version['schemas']['release-schema.json'][lang]):
        # If the field isn't removed.
        if field.schema is not None:
            continue

        original_field = _add_link_to_original_field(field, schema, sources)

        if original_field.get('deprecated'):
            group = 'deprecated'
        else:
            group = 'active'

        d = field.asdict(exclude=('definition_pointer', 'pointer', 'schema', 'required', 'deprecated', 'multilingual'))
        tables[group].append(d)

    return tables


def get_schema_tables(extension_version, lang):
    """
    Returns a dictionary of definition names and field tables. Each table is a list of fields. Each field is a
    dictionary with "definition_path", "path", "schema", "multilingual", "title", "description", "types" and "source"
    (if available) keys. All values are translated.

    The "description" (rendered from Markdown) and "types" values may contain HTML. The "description" includes any
    deprecation information.
    """
    tables = {}

    schema = _patch_schema(extension_version, 'en', include_test_dependencies=True)
    sources = _get_sources(schema, lang)

    for field in get_schema_fields(extension_version['schemas']['release-schema.json'][lang]):
        # If the field is removed.
        if field.schema is None:
            continue

        key = field.definition_path
        if not key:
            key = 'Release'

        if key not in tables:
            tables[key] = {'fields': []}
            if field.definition_path in sources:
                tables[key]['source'] = sources[field.definition_path]

        try:
            _add_link_to_original_field(field, schema, sources)
        except jsonpointer.JsonPointerException:
            pass

        d = field.asdict(sep='.', exclude=('definition_pointer', 'pointer', 'required', 'deprecated'))
        d['title'] = field.schema.get('title', '')
        d['description'] = commonmark(field.schema.get('description', ''))
        d['types'] = gettext(' or ').join(_get_types(field.schema, lang, sources))
        tables[key]['fields'].append(d)

    return tables


def _get_types(value, lang, sources):
    """
    Returns the types of the field, linking to definitions and iterating into arrays.
    """

    if '$ref' in value:
        name = value['$ref'][14:]  # remove '#/definitions/'
        if name in sources:
            url = sources[name]['url']
        else:
            url = '#{}'.format(name.lower())  # local definition
        return ['<a href="{}">{}</a> {}'.format(url, name, gettext('object'))]

    types = value.get('type', [])
    if isinstance(types, str):
        types = [types]

    # "type" might include "null" (valid JSON Schema) or `null` (invalid JSON Schema).
    types = list(filter(lambda t: t and t != 'null', types))

    # Make into sentence
    # 'uniqueItems',
    # 'wholeListMerge', # link to docs

    # Refer to codelist and ignore enum
    # 'codelist',
    # 'openCodelist',

    # Definition list
    # 'minimum',
    # 'maximum',
    # 'minLength',
    # 'maxLength',
    # 'minItems',
    # 'maxItems',
    # 'minProperties',
    # 'maxProperties',
    # 'format', # link to docs
    # 'enum', # if not codelist

    # Explain?
    # 'default',
    # 'pattern',

    if 'items' in value:
        # Avoid descending into /Amendment/changes, which will raise an error.
        if value.get('deprecated'):
            return types

        if types and types != ['array']:
            raise NotImplementedError("{} is not implemented".format(' / '.join(types)))
        if 'properties' in value['items']:
            raise NotImplementedError('array of objects with properties is not implemented: {!r}'.format(value))
        if 'items' in value['items']:
            raise NotImplementedError('array of arrays with items is not implemented: {!r}'.format(value))

        subtypes = ' / '.join('{}s'.format(_type) for _type in _get_types(value['items'], lang, sources))
        if subtypes:
            types = [gettext('array of %(subtypes)s') % {'subtypes': subtypes}]

    # Return object instead of simple list, do more work in template
    return types


def _add_link_to_original_field(field, schema, sources):
    original_field = jsonpointer.resolve_pointer(schema, field.pointer)

    field_url_prefix = sources[field.definition_path]['field_url_prefix']
    if field_url_prefix:
        field['url'] = field_url_prefix + field.pointer_components[-1]

    return original_field


def _ocds_codelist_names():
    """
    Returns the names of the codelists in the OCDS release schema.
    """
    return _ocds_codelist_names_recursive(_ocds_release_schema('en'))


# Similar to `collect_codelist_values` in `test_json.py` in standard-maintenance-scripts.
def _ocds_codelist_names_recursive(data):
    codelists = set()

    if isinstance(data, list):
        for item in data:
            codelists.update(_ocds_codelist_names_recursive(item))
    elif isinstance(data, dict):
        if 'codelist' in data:
            codelists.add(data['codelist'])

        for value in data.values():
            codelists.update(_ocds_codelist_names_recursive(value))

    return codelists


def _get_sources(schema, lang):
    extensions = get_extensions(get_extension_explorer_data_filename())

    release_reference_url = _ocds_release_reference_url(lang)
    core_field_url_prefix_template = '{}#release-schema.json,/definitions/{},'

    sources = {
        # Release
        '': {
            'type': 'core',
            'url': '{}#release'.format(release_reference_url),
            'field_url_prefix': '{}#release-schema.json,,'.format(release_reference_url)
        }
    }

    for name, definition in schema['definitions'].items():
        if 'extension_explorer:source' in definition:
            source = definition['extension_explorer:source']
            url = url_for('extension_schema', **source, lang=lang)

            sources[name] = {
                'type': 'extension',
                'url': '{}#{}'.format(url, name.lower()),
                'field_url_prefix': '{}#{}.'.format(url, name),
                'extension_name': extensions[source['identifier']]['name'][lang],
                'extension_url': url_for('extension_documentation', **source, lang=lang),
            }
        else:
            sources[name] = {
                'type': 'core',
                'url': '{}#{}'.format(release_reference_url, name.lower()),
            }

            # OCDS 1.1 doesn't list OrganizationReference's fields.
            if name == 'OrganizationReference':
                sources[name]['field_url_prefix'] = None
            else:
                sources[name]['field_url_prefix'] = core_field_url_prefix_template.format(release_reference_url, name)

    return sources


def _patch_schema(version, lang, include_test_dependencies=False):
    schema = deepcopy(_ocds_release_schema(lang))
    _patch_schema_recursive(schema, version, lang, include_test_dependencies=include_test_dependencies)
    return schema


def _patch_schema_recursive(schema, version, lang, include_test_dependencies=False):
    dependencies = version['metadata'].get('dependencies', [])
    if include_test_dependencies:
        dependencies += version['metadata'].get('testDependencies', [])

    extension_versions_by_base_url = _extension_versions_by_base_url()

    for url in dependencies:
        version = extension_versions_by_base_url[url[:-14]]  # remove "extension.json"
        patch = version['schemas']['release-schema.json'][lang]

        # Make it possible to determine the source of the definitions.
        for name, definition in patch.get('definitions', {}).items():
            if name not in schema['definitions']:
                definition['extension_explorer:source'] = {'identifier': version['id'], 'version': version['version']}

        json_merge_patch.merge(schema, patch)
        _patch_schema_recursive(schema, version, lang, include_test_dependencies=include_test_dependencies)


@lru_cache()
def _extension_versions_by_base_url():
    extensions = get_extensions(get_extension_explorer_data_filename())

    mapping = {}
    for extension in extensions.values():
        for version in extension['versions'].values():
            mapping[version['base_url']] = version
    return mapping


@lru_cache()
def _ocds_release_schema(lang):
    return requests.get(_ocds_release_schema_url(lang)).json()


def _ocds_release_schema_url(lang):
    return _ocds_documentation_url('{}/{}/release-schema.json', lang)


def _ocds_release_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/reference/', lang)


def _ocds_codelist_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/codelists/', lang)


def _ocds_documentation_url(template, lang):
    return template.format(OCDS_BASE_URL, lang)
