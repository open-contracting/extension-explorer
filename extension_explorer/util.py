from collections import defaultdict

import lxml.html
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify


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

    for element in root.iter('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
        slug = slugify(element.text)
        if slug in slug_counts:
            heading_id = '{}-{}'.format(slug, slug_counts[slug])
        else:
            heading_id = slug
        slug_counts[slug] += 1

        element.attrib['id'] = heading_id
        headings.append({'id': heading_id, 'level': int(element.tag[1]), 'text': element.text})

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
        new_pointer = pointer + key

        # Only core fields should lack titles and descriptions.
        if 'title' in value or 'description' in value:
            yield (definition, new_pointer, value.get('title', ''), value.get('description', ''), _get_types(value))

        if 'properties' in value:
            yield from _get_schema_fields(value, pointer=new_pointer, definition=definition)

    for key, value in schema.get('definitions', {}).items():
        yield from _get_schema_fields(value, definition=key)


def _get_types(value):
    if '$ref' in value:
        return value['$ref'].replace('#/definitions/', '')
    else:
        types = value.get('type', [])
        if isinstance(types, str):
            types = [types]

        # "type" might include "null" (valid JSON Schema) or `null` (invalid JSON Schema).
        types = ', '.join(filter(lambda t: t and t != 'null', types))

        if 'items' in value:
            if 'properties' in value['items']:
                raise NotImplementedError("arrays of objects with properties are not implemented")
            if 'items' in value['items']:
                raise NotImplementedError("arrays of arrays with items are not implemented")
            types += ' ({})'.format(_get_types(value['items']))

        return types
