"""
Module to keep ``views.py`` simple and high-level.
"""
import os
import json
from collections import defaultdict, OrderedDict
from functools import lru_cache, cmp_to_key
from glob import glob

import lxml.html
import requests
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify
from yaml import load

OCDS_BASE_URL = 'http://standard.open-contracting.org/1.1'
RELEASE_SCHEMA_URL = '{}/en/release-schema.json'.format(OCDS_BASE_URL)
RELEASE_SCHEMA_REFERENCE_URL = '{}/en/schema/reference/'.format(OCDS_BASE_URL)


def _compare_collections(a, b):
    a_type = a.get('type', '')
    b_type = b.get('type', '')
    a_title = a['title']
    b_title = b['title']
    if a_type < b_type:
        return -1
    elif a_type > b_type:
        return 1
    elif a_title < b_title:
        return -1
    else:
        return 1


@lru_cache()
def get_collections():
    """
    Returns the non-hidden collections of extensions, ordered by type and title.
    """
    collections = []

    filenames = glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'collections', '*.yaml'))
    for filename in filenames:
        with open(filename) as f:
            collection = load(f)
            if not collection.get('hidden'):
                collections.append(collection)

    return sorted(collections, key=cmp_to_key(_compare_collections))


@lru_cache()
def get_extensions():
    """
    Returns the data file's parsed contents. Set the file's path with the ``EXTENSION_EXPLORER_DATA_FILE`` environment
    variable (default is ``extension_explorer/data/extensions.json``).
    """
    if os.environ.get('EXTENSION_EXPLORER_DATA_FILE'):
        filename = os.environ.get('EXTENSION_EXPLORER_DATA_FILE')
    else:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'extensions.json')
    with open(filename) as f:
        return json.load(f, object_pairs_hook=OrderedDict)


@lru_cache()
def get_ocds_definitions():
    """
    Returns the names of the definitions in the OCDS release schema.
    """
    schema = requests.get(RELEASE_SCHEMA_URL).json()
    return list(schema['definitions'])


def get_extension_and_version(identifier, version):
    """
    Returns an extension and a version of it.
    """
    data = get_extensions()
    return data[identifier], data[identifier]['versions'][version]


def get_present_and_historical_versions(extension):
    """
    Returns the present and historical versions, with release dates.
    """
    latest_version = extension['latest_version']
    versions = extension['versions']

    historical_versions = [v for v in versions.values() if v['version'] != latest_version]
    historical_versions = sorted(historical_versions, key=lambda v: v['date'], reverse=True)
    historical_versions = [(v['version'], v['date']) for v in historical_versions]

    present_versions = [(latest_version, versions[latest_version]['date'])]
    # For now, only the most recent frozen release is a present version.
    if latest_version == 'master' and historical_versions and historical_versions[0][1]:
        present_versions.append(historical_versions.pop(0))

    return present_versions, historical_versions


def get_codelist_fieldname_indices(extension_version):
    """
    Returns a list of indices to fieldnames, to ensure that the default fieldnames always appear first.
    """
    codelist_fieldname_indices = {}

    for name, codelist in extension_version['codelists'].items():
        indices = [None, None, None]
        for i, fieldname in enumerate(codelist['en']['fieldnames']):
            for j, default in enumerate(('Code', 'Title', 'Description')):
                if fieldname == default:
                    indices[j] = i
                    break
            else:
                indices.append(i)
        codelist_fieldname_indices[name] = [index for index in indices if index is not None]

    return codelist_fieldname_indices


def get_schema_tables(extension_version, lang):
    """
    For each field in the schema, yields (definition, pointer, title, description, types).
    """
    tables = defaultdict(list)
    for definition, *rest in _get_schema_fields(extension_version['schemas']['release-schema.json'][lang]):
        tables[definition].append(rest)
    return tables


def identify_headings(html):
    """
    Adds `id` attributes to headings in the HTML. Returns the HTML, and a list of headings.
    """
    root = lxml.html.fromstring(html)

    headings = []
    slug_counts = defaultdict(int)
    previous_level = 1

    for element in root.iter('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        heading_level = int(element.tag[1])

        # Fix skipped heading levels.
        if heading_level > previous_level:
            heading_level = previous_level + 1

        # Skip changelog sub-headings.
        if headings and headings[-1]['text'] == 'Changelog' and previous_level < heading_level:
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


# This code is similar to `add_versioned` in `make_versioned_release_schema.py` in the `standard` repository.
def _get_schema_fields(schema, pointer='', definition='Release'):
    """
    For each field in the schema, yields (definition, pointer, title, description, types).
    """
    # Omit the initial "/" for brevity.
    if pointer:
        pointer += '/'

    for key, value in schema.get('properties', {}).items():
        # If the extension deletes fields.
        if value is None:
            continue

        new_pointer = pointer + key

        # Only core fields should lack titles and descriptions.
        if 'title' in value or 'description' in value or 'deprecated' in value:
            title = value.get('title', '')
            description = value.get('description', '')
            types = ' or '.join(_get_types(value))

            if 'deprecated' in value:
                deprecated = value['deprecated']
                if deprecated:
                    message = 'Deprecated in OCDS {}. {}'.format(deprecated['deprecatedVersion'], deprecated['description'])  # noqa
                else:
                    message = 'Undeprecated'
                description += '<p><em>{}</em></p>'.format(message)

            yield (definition, new_pointer, title, description, types)

        if 'properties' in value:
            yield from _get_schema_fields(value, pointer=new_pointer, definition=definition)

    for key, value in schema.get('definitions', {}).items():
        yield from _get_schema_fields(value, definition=key)


def _get_types(value):
    definitions = get_ocds_definitions()

    if '$ref' in value:
        name = value['$ref'].replace('#/definitions/', '')
        if name in definitions:
            url = RELEASE_SCHEMA_REFERENCE_URL
        else:
            url = ''
        return ['<a href="{}#{}">{}</a> object'.format(url, name.lower(), name)]
    else:
        types = value.get('type', [])
        if isinstance(types, str):
            types = [types]

        # "type" might include "null" (valid JSON Schema) or `null` (invalid JSON Schema).
        types = list(filter(lambda t: t and t != 'null', types))

        if 'items' in value:
            if types and types != ['array']:
                raise NotImplementedError("{} is not implemented".format(' / '.join(types)))
            if 'properties' in value['items']:
                raise NotImplementedError('array of objects with properties is not implemented')
            if 'items' in value['items']:
                raise NotImplementedError('array of arrays with items is not implemented')
            types = ['array of {}'.format(' / '.join('{}s'.format(_type) for _type in _get_types(value['items'])))]

        return types
