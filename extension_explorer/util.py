"""Module to keep ``views.py`` simple and high-level."""
import contextlib
import json
import os
import re
from collections import defaultdict
from copy import deepcopy
from functools import lru_cache

import json_merge_patch
import jsonpointer
import lxml.html
import requests
from flask import url_for
from flask_babel import gettext, ngettext
from markdown_it import MarkdownIt
from ocdsextensionregistry.util import remove_nulls
from ocdskit.schema import get_schema_fields
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify
from yaml import safe_load

OCDS_BASE_URL = 'https://standard.open-contracting.org/1.1'
LANGUAGE_CODE_SUFFIX = '_(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-(x(-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+))'  # noqa: E501
LANGUAGE_CODE_SUFFIX_LEN = len(LANGUAGE_CODE_SUFFIX)


def markdown(md):
    """Render Markdown text as HTML."""
    parser = MarkdownIt('default')
    env = {}

    tokens = parser.parse(md, env)
    for token in tokens:
        if token.type == 'table_open':
            token.attrs = {'class': 'table table-bordered'}
        elif token.type == 'thead_open':
            token.attrs = {'class': 'table-light'}
        elif token.type == 'th_open':
            token.attrs = {'scope': 'col'}

    return parser.renderer.render(tokens, parser.options, env)


def get_extension_explorer_data_filename():
    """
    Return the data file's path.

    Set it with the ``EXTENSION_EXPLORER_DATA_FILENAME`` environment variable (default:
    ``extension_explorer/data/extensions.json``).
    """
    if os.getenv('EXTENSION_EXPLORER_DATA_FILENAME'):
        return os.getenv('EXTENSION_EXPLORER_DATA_FILENAME')
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'extensions.json')


@lru_cache
def get_extensions(filename=None):
    """Return the data file's parsed contents."""
    if not filename:
        filename = get_extension_explorer_data_filename()
    with open(filename) as f:
        return json.load(f)


def set_tags(extensions):
    """Add tags and publishers to extensions, and return profile, topic and publisher tags."""
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'tags.yaml')) as f:
        data = safe_load(f)

    for extension in extensions.values():
        extension['tags'] = set()
        if extension['core']:
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
                    extensions[identifier]['tags'].add(f'{prefix}-{slug}')
            groups[prefix][slug] = tag['title']

    publishers = {}
    for extension in extensions.values():
        latest_version = extension['latest_version']
        publisher = extension['versions'][latest_version]['publisher']
        extension['publisher'] = publisher

        slug = slugify(publisher['name'])
        extension['tags'].add(f'publisher-{slug}')
        publishers[slug] = publisher['name']

    return groups['profile'], groups['topic'], publishers


def get_present_and_historical_versions(extension):
    """Return the present and historical versions, with release dates, in reverse chronological order."""
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
    """Add `id` attributes to headings in the HTML, skipping any changelog sub-headings. Return HTML and headings."""
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

        slug = slugify(element.text_content())
        heading_id = f'{slug}-{slug_counts[slug]}' if slug in slug_counts else slug
        element.attrib['id'] = heading_id

        headings.append({'id': heading_id, 'level': heading_level, 'text': element.text_content()})
        slug_counts[slug] += 1
        previous_level = heading_level

    html = lxml.html.tostring(root).decode()

    return html, headings


def highlight_json(html):
    """Highlight JSON code blocks. Return the HTML, and the CSS for highlighting."""
    root = lxml.html.fromstring(html)

    for code_block in root.find_class('language-json'):
        replacement = lxml.html.fromstring(highlight(code_block.text, JsonLexer(), HtmlFormatter()))
        parent = code_block.getparent()
        parent.getparent().replace(parent, replacement)

    html = lxml.html.tostring(root).decode()

    return html, HtmlFormatter().get_style_defs('.highlight')


def get_codelist_tables(extension_version, lang):
    """
    Return a list of tables, one per codelist. Each item is a list of the codelist's name, basename, documentation URL
    (if patched), translated fieldnames, and and translated rows. Each row is a dictionary with up to three keys:
    "code", "title" and "content". The "content" value is a dictionary with "description" and "attributes" keys. The
    "description" value is the Description column value rendered from Markdown. The "attributes" value is a dictionary
    of additional column headers and values.

    The "description" value (rendered from Markdown) may contain HTML. The code supports old-style column headers like
    "Title_en" and "Description_en".
    """
    tables = []

    header_groups = (('Code',), ('Title', 'Title_en'), ('Description', 'Description_en'))

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
                content['description'] = markdown(row[fieldname_map['Description']])

            attributes = {k: v for k, v in sorted(row.items()) if k not in fieldnames and v}
            if attributes:
                content['attributes'] = attributes

            if content:
                new_row['content'] = content
                # Add the column if the row has no description, but other attributes.
                if 'Description' not in fieldname_map:
                    fieldnames.append(gettext('Description'))

            rows.append(new_row)

        basename = name[1:] if name.startswith(('+', '-')) else name

        url = _codelist_url(basename, extension_version, lang)

        tables.append([name, basename, url, fieldnames, rows])

    return tables


def get_schema_tables(extension_version, lang):
    """
    Return a dictionary of definition names and field tables. Each table is a list of fields.
    All values are translated.

    The "description" (rendered from Markdown) and "types" values may contain HTML. The "description" includes any
    deprecation information.
    """
    tables = {}

    if not extension_version['schemas']['release-schema.json']:
        return tables

    schema = _patch_schema(extension_version, 'en', include_test_dependencies=True)
    sources = _get_sources(schema, lang)

    patch = extension_version['schemas']['release-schema.json'][lang]
    remove_nulls(patch)

    for field in get_schema_fields(patch):
        # If the field is removed.
        if field.schema is None:
            continue

        key = field.definition
        if not key:
            key = 'Release'

        if key not in tables:
            tables[key] = {'fields': []}
            if field.definition in sources:
                tables[key]['source'] = sources[field.definition]

        d = field.asdict(
            sep='.',
            exclude=('name', 'deprecated_self', 'deprecated', 'pointer', 'pattern', 'required', 'merge_by_id'),
        )
        with contextlib.suppress(jsonpointer.JsonPointerException):
            _, d['url'] = _add_link_to_original_field(field, schema, sources)
        d['title'] = field.schema.get('title', '')
        d['description'] = markdown(field.schema.get('description', ''))
        d['types'] = gettext(' or ').join(_get_types(field.schema, sources, extension_version, lang))

        tables[key]['fields'].append(d)

    return tables


def _get_types(value, sources, extension_version, lang, n=1, field=None):
    """Return the types of the field, linking to definitions and iterating into arrays."""
    if '$ref' in value:
        name = value['$ref'][14:]  # remove '#/definitions/'
        url = sources[name]['url'] if name in sources else f'#{name.lower()}'  # local definition
        noun = ngettext('object', 'objects', n)
        return [f'<a href="{url}">{name}</a> {noun}']

    types = value.get('type', [])
    if isinstance(types, str):
        types = [types]

    # "type" might include "null" (valid JSON Schema) or `null` (invalid JSON Schema).
    types = [t for t in types if t and t != 'null']

    if field and 'codelist' in field:
        codelist_schema = field
    elif not field and 'codelist' in value:
        codelist_schema = value
    else:
        codelist_schema = {}

    if 'codelist' in codelist_schema and types == ['string']:
        codelist = codelist_schema['codelist']
        open_codelist = codelist_schema['openCodelist']
        variables = {
            'url': _codelist_url(codelist, extension_version, lang),
            'codelist': os.path.splitext(codelist)[0],
        }
        if open_codelist is True:
            return [ngettext('string from open <a href="%(url)s">%(codelist)s</a> codelist',
                             'strings from open <a href="%(url)s">%(codelist)s</a> codelist', n, **variables)]
        if open_codelist is False:
            return [ngettext('string from closed <a href="%(url)s">%(codelist)s</a> codelist',
                             'strings from closed <a href="%(url)s">%(codelist)s</a> codelist', n, **variables)]
        return [ngettext('string from <a href="%(url)s">%(codelist)s</a> codelist',
                         'strings from <a href="%(url)s">%(codelist)s</a> codelist', n, **variables)]

    types = [ngettext('%(type)s', '%(type)ss', n, type=t) for t in types]

    # Make into sentence
    # 'uniqueItems',
    # 'wholeListMerge', # link to docs

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
    # 'pattern',

    if 'items' in value:
        # Avoid descending into /Amendment/changes, which will raise an error.
        if value.get('deprecated'):
            return types

        if types and types != ['array']:
            raise NotImplementedError(f"{' / '.join(types)} is not implemented")
        if 'properties' in value['items']:
            raise NotImplementedError(f'array of objects with properties is not implemented: {value!r}')
        if 'items' in value['items']:
            raise NotImplementedError(f'array of arrays with items is not implemented: {value!r}')

        subtypes = ' / '.join(_get_types(value['items'], sources, extension_version, lang, field=value, n=2))
        if subtypes:
            types = [gettext('array of %(subtypes)s') % {'subtypes': subtypes}]

    # Return object instead of simple list, do more work in template
    return types


def _add_link_to_original_field(field, schema, sources):
    original_field = jsonpointer.resolve_pointer(schema, field.pointer)

    field_url_prefix = sources[field.definition]['field_url_prefix']
    url = field_url_prefix + field.name if field_url_prefix else None

    return original_field, url


def _codelist_url(basename, extension_version, lang):
    codelist_reference_url = _ocds_codelist_reference_url(lang)
    codelist_names = _ocds_codelist_names()

    url = None
    if basename in extension_version['codelists']:
        url = url_for('extension_codelists', lang=lang, identifier=extension_version['id'],
                      version=extension_version['version'], _anchor=basename)
    elif basename in codelist_names:
        anchor = re.sub(r'[A-Z]', lambda s: '-' + s[0].lower(), os.path.splitext(basename)[0])
        url = f'{codelist_reference_url}#{anchor}'
    # TODO(james): Hardcoding for ocds_statistics_extension.
    # https://github.com/open-contracting/extension-explorer/issues/58
    elif basename == 'statistic.csv':
        url = url_for('extension_codelists', lang=lang, identifier='bids', version='master', _anchor=basename)
    else:
        raise NotImplementedError(f"linking to another extension's codelist is not implemented: {basename}")

    return url


@lru_cache
def _ocds_codelist_names():
    """Return the names of the codelists in the OCDS release schema."""
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
            'url': f'{release_reference_url}#release',
            'field_url_prefix': f'{release_reference_url}#release-schema.json,,'
        }
    }

    for name, definition in schema['definitions'].items():
        if 'extension_explorer:source' in definition:
            source = definition['extension_explorer:source']
            url = url_for('extension_schema', **source, lang=lang)

            sources[name] = {
                'type': 'extension',
                'url': f'{url}#{name.lower()}',
                'field_url_prefix': f'{url}#{name}.',
                'extension_name': extensions[source['identifier']]['name'][lang],
                'extension_url': url_for('extension_documentation', **source, lang=lang),
            }
        else:
            sources[name] = {
                'type': 'core',
                'url': f'{release_reference_url}#{name.lower()}',
            }

            # OCDS 1.1 doesn't list OrganizationReference's fields.
            if name == 'OrganizationReference':
                sources[name]['field_url_prefix'] = None
            else:
                sources[name]['field_url_prefix'] = core_field_url_prefix_template.format(release_reference_url, name)

    return sources


def _patch_schema(version, lang, *, include_test_dependencies=False):
    schema = deepcopy(_ocds_release_schema(lang))
    _patch_schema_recursive(schema, version, lang, include_test_dependencies=include_test_dependencies)
    return schema


def _patch_schema_recursive(schema, version, lang, *, include_test_dependencies=False):
    dependencies = version['metadata'].get('dependencies', [])
    if include_test_dependencies:
        dependencies += version['metadata'].get('testDependencies', [])

    extension_versions_by_base_url = _extension_versions_by_base_url()

    for url in dependencies:
        version = extension_versions_by_base_url[url[:-14]]  # remove "extension.json"

        patch = version['schemas']['release-schema.json'][lang]
        remove_nulls(patch)

        # Make it possible to determine the source of the definitions.
        for name, definition in patch.get('definitions', {}).items():
            if name not in schema['definitions']:
                definition['extension_explorer:source'] = {'identifier': version['id'], 'version': version['version']}

        json_merge_patch.merge(schema, patch)
        _patch_schema_recursive(schema, version, lang, include_test_dependencies=include_test_dependencies)


@lru_cache
def _extension_versions_by_base_url():
    extensions = get_extensions(get_extension_explorer_data_filename())

    mapping = {}
    for extension in extensions.values():
        for version in extension['versions'].values():
            mapping[version['base_url']] = version
    return mapping


@lru_cache
def _ocds_release_schema(lang):
    response = requests.get(_ocds_release_schema_url(lang), timeout=10)
    response.raise_for_status()
    return response.json()


def _ocds_release_schema_url(lang):
    return _ocds_documentation_url('{}/{}/release-schema.json', lang)


def _ocds_release_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/reference/', lang)


def _ocds_codelist_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/codelists/', lang)


def _ocds_documentation_url(template, lang):
    return template.format(OCDS_BASE_URL, lang)
