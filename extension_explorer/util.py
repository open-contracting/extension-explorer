import re
from collections import defaultdict

import lxml.html
from lxml.html import builder as E
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import JsonLexer
from slugify import slugify

directive_name_pattern = re.compile(r'^\.\. ([^:]+)::$')
option_pattern = re.compile(r'^:([^:]+):(.*)$')


def get_extension_tables(extension_version, lang):
    extension_tables = defaultdict(list)
    for row in gather_fields(extension_version['release_schema'][lang]):
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
        _replace_parent(code_block, lxml.html.fromstring(highlight(code_block.text, JsonLexer(), HtmlFormatter())))

    html = lxml.html.tostring(root).decode()

    return html, HtmlFormatter().get_style_defs('.highlight')


def replace_directives(html, schema_url, codelist_url, extension_tables):
    """
    Replaces RST code blocks with links to schema and codelist reference tables. Returns the HTML.
    """
    root = lxml.html.fromstring(html)

    for code_block in root.find_class('language-eval_rst'):
        lines = code_block.text.strip().split('\n')
        if lines:
            replacement = None
            directive_name = get_directive_name(lines)

            if directive_name == 'extensiontable':
                replacement = extensiontable_replacement(lines, schema_url, extension_tables)
            elif directive_name in ('csv-table-no-translate', 'csv-table'):
                replacement = csv_table_replacement(lines, codelist_url)
            else:
                raise NotImplementedError('Unknown directive: {}'.format(directive_name))

            if replacement:
                _replace_parent(code_block, replacement)
            else:
                _remove_parent(code_block)

    html = lxml.html.tostring(root).decode()

    return html


def extensiontable_replacement(lines, url, extension_tables):
    options = get_directive_options(lines, ['extension', 'definitions', 'exclude_definitions'])

    # TODO
    # Don't include release (top) level fields they are indicated by empty string
    definitions = [definition for definition in extension_tables if definition]

    if 'definitions' in options:
        whitelist = options['definitions'].split()
        definitions = [d for d in definitions if d in whitelist]

    if 'exclude_definitions' in options:
        blacklist = options['exclude_definitions'].split()
        definitions = [d for d in definitions if d not in blacklist]

    if not definitions:
        return  # remove the directive

    list_items = []
    for definition in definitions:
        href = '{}#{}'.format(url, definition)
        list_items.append(E.LI(E.A(definition, E.I(E.CLASS('fas fa-external-link-alt ml-2 small-icon')), href=href)))

    return E.BLOCKQUOTE(E.CLASS('blockquote'), E.UL(E.CLASS('list-unstyled'), *list_items))


def csv_table_replacement(lines, url):
    options = get_directive_options(lines, ['file', 'header-rows'])
    codelist_filename = options['file'].rsplit('/', 1)[-1]

    href = '{}#{}'.format(url, codelist_filename)
    a = E.A(codelist_filename, E.I(E.CLASS('fas fa-external-link-alt ml-2 small-icon')), href=href)

    return E.BLOCKQUOTE(E.CLASS('blockquote'), a)


def get_directive_name(lines):
    """
    Returns the directive's name.
    """
    match = directive_name_pattern.search(lines[0].strip())
    if match:
        return match.group(1)


def get_directive_options(lines, known_option_names=[]):
    """
    Returns the directive's known options.
    """
    # We can't use docutils' parser, because it errors if, e.g., an option value is a non-existent file. To use only
    # parts of its parser to circumvent such errors, we'd have to simulate or re-implement its state machine. Instead,
    # we use a simplistic parser.
    #
    # http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#directives
    # http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#field-lists
    options = {}

    for line in lines[1:]:
        line = line.strip()
        match = option_pattern.search(line)
        if match:
            option_name = match.group(1)
            if option_name in known_option_names:
                options[option_name] = match.group(2).strip()
            else:
                raise NotImplementedError('Unknown option: {}'.format(option_name))
        else:
            raise NotImplementedError('Unexpected line: {}'.format(line))

    return options


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


def _replace_parent(element, replacement):
    parent = element.getparent()
    parent.getparent().replace(parent, replacement)


def _remove_parent(element, replacement):
    parent = element.getparent()
    parent.getparent().replace(parent)
