from collections import defaultdict

import lxml.html
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify


def get_extension_tables(extension_version, lang):
    extension_tables = defaultdict(list)
    for row in gather_fields(extension_version['schemas']['release-schema.json'][lang]):
        definition = row[0]
        if not definition:
            definition = 'Release'
        extension_tables[definition].append(row[1:])
    return extension_tables


def mark_headings(html):
    """
    Adds `id` attributes to h1-h5 headings in the HTML. Returns the HTML, and a list of headings.
    """
    root = lxml.html.fromstring(html)

    headings = []
    slug_counts = defaultdict(int)

    for element in root.iter('h1', 'h2', 'h3', 'h4', 'h5'):
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


def gather_fields(schema, path='', definition=''):
    if 'properties' in schema:
        for field_name, field_info in schema['properties'].items():
            if not field_info:
                continue

            yield from gather_fields(field_info, path + '/' + field_name, definition=definition)
            for key, value in field_info.items():
                if isinstance(value, dict):
                    yield from gather_fields(value, path + '/' + field_name, definition=definition)

            types = field_info.get('type', '')
            if isinstance(types, list):
                types = ', '.join(types).replace(', null', '').replace('null,', '')
            else:
                types = types

            if not types:
                types = field_info.get('$ref', '').replace('#/definitions/', '')

            description = field_info.get('description')
            if description:
                yield [
                    definition,
                    (path + '/' + field_name).lstrip('/'),
                    field_info.get('title', ''),
                    description,
                    types,
                ]

    if 'definitions' in schema:
        for key, value in schema['definitions'].items():
            yield from gather_fields(value, definition=key)
