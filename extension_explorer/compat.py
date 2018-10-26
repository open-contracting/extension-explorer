import re

import lxml.html
from lxml.html import builder as E

from .util import _replace_parent, _remove_parent

directive_name_pattern = re.compile(r'^\.\. ([^:]+)::$')
option_pattern = re.compile(r'^:([^:]+):(.*)$')


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
