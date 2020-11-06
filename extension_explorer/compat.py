"""
Methods for compatibility with older versions of extensions' documentation, which used Sphinx directives.
"""
import re

import lxml.html
from flask_babel import gettext
from lxml.html import builder as E

directive_name_pattern = re.compile(r'^\.\. ([^:]+)::$')
option_pattern = re.compile(r'^:([^:]+):(.*)$')


def replace_directives(html, schema_url, codelist_url, tables):
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
                if schema_url:
                    replacement = get_extensiontable_replacement(lines, schema_url, tables)
            elif directive_name in ('csv-table-no-translate', 'csv-table'):
                replacement = get_csv_table_replacement(lines, codelist_url)
            elif directive_name:
                raise NotImplementedError('Unknown directive: {}'.format(directive_name))
            else:
                raise NotImplementedError('Unexpected line: {}'.format(lines[0]))

            parent = code_block.getparent()
            if replacement is not None:
                parent.getparent().replace(parent, replacement)
            else:
                parent.getparent().remove(parent)

    html = lxml.html.tostring(root).decode()

    return html


def get_extensiontable_replacement(lines, url, tables):
    """
    Returns a link to a section of the schema reference.
    """
    options = get_directive_options(lines, ['extension', 'definitions', 'exclude_definitions'])

    definitions = list(tables)

    # The original implementation would error if both `definitions` and `exclude_definitions` were set. Here, we
    # instead apply the whitelist and then the blacklist, to avoid an error.
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
        href = '{}#{}'.format(url, definition.lower())
        text = gettext('View the fields in the %(definition)s object') % {'definition': definition}
        list_items.append(E.LI(E.A(text, href=href)))

    return E.UL(E.CLASS('list-unstyled'), *list_items)


def get_csv_table_replacement(lines, url):
    """
    Returns a link to a section of the codelists reference.
    """
    options = get_directive_options(lines, ['file', 'header-rows'])
    codelist = options['file'].rsplit('/', 1)[-1]

    href = '{}#{}'.format(url, codelist)
    text = gettext('View the codes in the %(codelist)s codelist') % {'codelist': codelist}
    return E.P(E.A(text, href=href))


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
        if not match:
            raise NotImplementedError('Unexpected line: {}'.format(line))

        option_name = match.group(1)
        if option_name not in known_option_names:
            raise NotImplementedError('Unknown option: {}'.format(option_name))

        options[option_name] = match.group(2).strip()

    return options
