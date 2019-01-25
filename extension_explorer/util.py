"""
Module to keep ``views.py`` simple and high-level.
"""
import json
import os
import re
import warnings
from collections import defaultdict, OrderedDict
from functools import lru_cache

import jsonpointer
import lxml.html
import requests
from CommonMark import DocParser, HTMLRenderer
from flask_babel import gettext
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify
from yaml import load

OCDS_BASE_URL = 'http://standard.open-contracting.org/1.1'
LANGUAGE_CODE_PATTERN = '_(((([A-Za-z]{2,3}(-([A-Za-z]{3}(-[A-Za-z]{3}){0,2}))?)|[A-Za-z]{4}|[A-Za-z]{5,8})(-([A-Za-z]{4}))?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-([0-9A-WY-Za-wy-z](-[A-Za-z0-9]{2,8})+))*(-(x(-[A-Za-z0-9]{1,8})+))?)|(x(-[A-Za-z0-9]{1,8})+)))$'  # noqa


def commonmark(text):
    """
    Renders text as Markdown.
    """
    parser = DocParser()
    ast = parser.parse(text)
    renderer = HTMLRenderer()

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
def get_extensions():
    """
    Returns the data file's parsed contents.
    """
    filename = get_extension_explorer_data_filename()
    with open(filename) as f:
        return json.load(f, object_pairs_hook=OrderedDict)


def set_tags(extensions):
    """
    Adds tags and publishers to extensions, and returns profile, topic and publisher tags.
    """
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'tags.yaml')) as f:
        data = load(f)

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


def get_extension_and_version(identifier, version):
    """
    Returns an extension and a version of it.
    """
    extensions = get_extensions()
    return extensions[identifier], extensions[identifier]['versions'][version]


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
    'code', 'title' and 'content'. The 'content' value is a dictionary with 'description' and 'attributes' keys. The
    'description' value is the Description column value rendered from Markdown. The 'attributes' value is a dictionary
    of additional column headers and values.
    """
    tables = []

    header_groups = (('Code',), ('Title', 'Title_en'), ('Description', 'Description_en'))
    codelist_reference_url = _ocds_codelist_reference_url(lang)
    codelist_names = _ocds_codelist_names(lang)

    for name, codelist in extension_version['codelists'].items():
        indices = {fieldname: i for i, fieldname in enumerate(codelist['en']['fieldnames'])}

        fieldname_map = OrderedDict()
        for header_group in header_groups:
            canonical_header = header_group[0]
            for header in header_group:
                if header in indices:
                    fieldname_map[canonical_header] = codelist[lang]['fieldnames'][indices[header]]
                    break

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
    dictionary with "definition", "path" and "url" (if available) keys. All values are translated.
    """
    tables = defaultdict(list)

    release_schema_reference_url = _ocds_release_schema_reference_url(lang)
    template = '{}#release-schema.json,{},{}'

    release_schema = _ocds_release_schema(lang)
    for field in _get_removed_fields(extension_version['schemas']['release-schema.json'][lang]):
        try:
            value = jsonpointer.resolve_pointer(release_schema, field['pointer'])

            # OCDS 1.1 doesn't list OrganizationReference's fields.
            if field['definition_pointer'] != '/definitions/OrganizationReference':
                # This depends on the implementation of the `jsonschema` Sphinx directive.
                field['url'] = template.format(release_schema_reference_url, field['definition_pointer'],
                                               field['pointer'].rsplit('/', 1)[-1])
        except jsonpointer.JsonPointerException:
            value = {}

        if value.get('deprecated'):
            group = 'deprecated'
        else:
            group = 'active'

        for key in ('definition_pointer', 'pointer'):
            del field[key]

        tables[group].append(field)

    return tables


def _get_removed_fields(schema, pointer='', path='', definition_pointer='', definition_path=''):
    pointer += '/'
    path += '.'

    for key, value in schema.get('properties', {}).items():
        new_pointer = pointer + 'properties/' + key
        new_path = path + key

        if value is None:
            yield {'definition_pointer': definition_pointer, 'definition_path': definition_path,
                   'pointer': new_pointer, 'path': new_path}
        elif 'properties' in value:
            yield from _get_removed_fields(value, pointer=new_pointer, path=new_path,
                                           definition_pointer=definition_pointer, definition_path=definition_path)

    for key, value in schema.get('definitions', {}).items():
        new_pointer = pointer + 'definitions/' + key
        new_path = path + key

        yield from _get_removed_fields(value, pointer=new_pointer, path=new_path,
                                       definition_pointer=new_pointer, definition_path=key)


def get_schema_tables(extension_version, lang):
    """
    Returns a dictionary of definition names and field tables. Each table is a list of fields. Each field is a
    dictionary with "definition", "path", "schema", "multilingual", "title", "description", and "types" keys.
    All values are translated.

    The "description" (rendered from Markdown) and "types" values may contain HTML. The "description" includes any
    deprecation information.
    """
    tables = defaultdict(list)

    for field in _get_schema_fields(extension_version['schemas']['release-schema.json'][lang], lang):
        tables[field['definition']].append(_add_title_description_types(field, field['schema'], lang))

    return tables


# This code is similar to `add_versioned` in `make_versioned_release_schema.py` in the `standard` repository.
def _get_schema_fields(schema, lang, path='', definition=None):
    path += '.'

    if definition is None:
        definition = gettext('Release')

    multilingual = set()
    for key, value in schema.get('patternProperties', {}).items():
        if LANGUAGE_CODE_PATTERN in key:
            multilingual.add(key.replace(LANGUAGE_CODE_PATTERN, '').replace('^(', ''))

    for key, value in schema.get('properties', {}).items():
        # If the extension deletes fields.
        if value is None:
            continue

        new_path = path + key
        yield {'definition': definition, 'path': new_path, 'schema': value, 'multilingual': key in multilingual}

        if 'properties' in value or 'patternProperties' in value:
            yield from _get_schema_fields(value, lang, path=new_path, definition=definition)

        # Per make_versioned_release_schema.py, un-$ref'erenced objects in arrays don't occur.

    for key, value in schema.get('definitions', {}).items():
        yield from _get_schema_fields(value, lang, definition=key)

    for key, value in schema.get('patternProperties', {}).items():
        if LANGUAGE_CODE_PATTERN not in key:
            new_path = '{}({})'.format(path, key)
            yield {'definition': definition, 'path': new_path, 'schema': value, 'multilingual': False}


def _get_types(value, lang):
    """
    Returns the types of the field, linking to definitions and iterating into arrays.
    """
    definitions = _ocds_release_schema_definitions(lang)

    if '$ref' in value:
        name = value['$ref'].replace('#/definitions/', '')
        if name in definitions:
            url = _ocds_release_schema_reference_url(lang)
        else:
            url = ''
        return ['<a href="{}#{}">{}</a> {}'.format(url, name.lower(), name, gettext('object'))]

    types = value.get('type', [])
    if isinstance(types, str):
        types = [types]

    # "type" might include "null" (valid JSON Schema) or `null` (invalid JSON Schema).
    types = list(filter(lambda t: t and t != 'null', types))

    if 'items' in value:
        # Avoid descending into /Amendment/changes, which will raise an error.
        if value.get('deprecated'):
            return types

        if types and types != ['array']:
            raise NotImplementedError("{} is not implemented".format(' / '.join(types)))
        if 'properties' in value['items']:
            raise NotImplementedError('array of objects with properties is not implemented: {}'.format(repr(value)))
        if 'items' in value['items']:
            raise NotImplementedError('array of arrays with items is not implemented: {}'.format(repr(value)))

        subtypes = ' / '.join('{}s'.format(_type) for _type in _get_types(value['items'], lang))
        if subtypes:
            types = [gettext('array of %(subtypes)s') % {'subtypes': subtypes}]

    return types


def _add_title_description_types(field, value, lang):
    field['title'] = value.get('title', '')
    field['description'] = value.get('description', '')
    field['types'] = gettext(' or ').join(_get_types(value, lang))

    if 'deprecated' in value:
        deprecated = value['deprecated']
        if deprecated:
            label = gettext('Deprecated in OCDS %(deprecatedVersion)s') % deprecated
            message = '**{}**: {}'.format(label, deprecated['description'])
        else:
            message = '*{}*'.format(gettext('Undeprecated'))
        field['description'] += '\n\n{}'.format(message)

    field['description'] = commonmark(field['description'])

    return field


def _ocds_release_schema_definitions(lang):
    """
    Returns the names of the definitions in the OCDS release schema.
    """
    return list(_ocds_release_schema(lang)['definitions'])


def _ocds_codelist_names(lang):
    """
    Returns the names of the codelists in the OCDS release schema.
    """
    return _ocds_codelist_names_recursive(_ocds_release_schema(lang))


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


@lru_cache()
def _ocds_release_schema(lang):
    """
    Returns the translated OCDS release schema.
    """
    return requests.get(_ocds_release_schema_url(lang)).json()


def _ocds_release_schema_url(lang):
    return _ocds_documentation_url('{}/{}/release-schema.json', lang)


def _ocds_release_schema_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/reference/', lang)


def _ocds_codelist_reference_url(lang):
    return _ocds_documentation_url('{}/{}/schema/codelists/', lang)


def _ocds_documentation_url(template, lang):
    return template.format(OCDS_BASE_URL, lang)
