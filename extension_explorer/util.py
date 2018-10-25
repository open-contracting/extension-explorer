from collections import defaultdict, Counter

import lxml.html
from lxml.html import builder as E
from slugify import slugify
from flask import url_for
from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import HtmlFormatter


def create_toc(html):

    root = lxml.html.fromstring(html)

    headings = []
    heading_count = Counter()

    for element in root.iter("h1", "h2", "h3", "h4", "h5"):
        heading_id = slugify(element.text)
        heading_count.update([heading_id])
        # This checks if there are duplicate headings and if so adds a number to the heading
        if heading_count[heading_id] > 1:
            heading_id = "{}-{}".format(heading_id, heading_count[heading_id])

        element.attrib['id'] = heading_id
        headings.append({"id": heading_id, "header_number": element.tag[1], "text": element.text})

    html = lxml.html.tostring(root).decode()

    return html, headings


def create_extension_tables(extension_version, lang):
    extension_tables = defaultdict(list)
    for row in gather_fields(extension_version['release_schema'][lang]):
        definition = row[0]
        if not definition:
            definition = "Release"
        extension_tables[definition].append(row[1:])
    return extension_tables


def highlight_json(html):
    root = lxml.html.fromstring(html)
    for code_block in root.find_class("language-json"):
        code_text = code_block.text

        higlighted = lxml.html.fromstring(highlight(code_text, JsonLexer(), HtmlFormatter()))
        pre_block = code_block.getparent()
        pre_block.getparent().replace(pre_block, higlighted)

    html = lxml.html.tostring(root).decode()

    return html, HtmlFormatter().get_style_defs('.highlight')


def replace_directives(html, extension_tables, lang, slug, version):

    root = lxml.html.fromstring(html)
    for code_block in root.find_class("language-eval_rst"):
        lines = code_block.text.strip().split('\n')
        if not lines:
            continue
        pre_block = code_block.getparent()
        replace_extensiontable_directive(pre_block, lines, extension_tables, lang, slug, version)
        replace_codelist_directive(pre_block, lines, lang, slug, version)

    html = lxml.html.tostring(root).decode()
    return html


def gather_fields(json, path="", definition=""):
    properties = json.get('properties')
    if properties:
        for field_name, field_info in properties.items():
            if not field_info:
                continue
            yield from gather_fields(field_info, path + '/' + field_name, definition=definition)
            for key, value in field_info.items():
                if isinstance(value, dict):
                    yield from gather_fields(value, path + '/' + field_name, definition=definition)

            types = field_info.get('type', '')
            if isinstance(types, list):
                types = ", ".join(types).replace(", null", "").replace("null,", "")
            else:
                types = types

            if not types:
                types = field_info.get('$ref', '').replace('#/definitions/', '')

            description = field_info.get("description")
            if description:
                yield [
                    definition,
                    (path + '/' + field_name).lstrip("/"),
                    field_info.get('title', ''),
                    description,
                    types,
                ]

    definitions = json.get('definitions')
    if definitions:
        for key, value in definitions.items():
            yield from gather_fields(value, definition=key)


def get_directive_arg(line, arg):
    stripped = line.strip()
    full_arg = ":" + arg + ":"
    if not stripped.startswith(full_arg):
        return
    return stripped[len(full_arg):].strip()


def replace_extensiontable_directive(pre_block, directive_lines, extension_tables, lang, slug, version):
    if not directive_lines[0].strip() == '.. extensiontable::':
        return False
    args = process_extensiontable(directive_lines[1:])

    # Dont include release (top) level fields they are indicated by empty string
    included_definitions = [definition for definition in extension_tables if definition]

    definitions = args.get('definitions')
    if definitions:
        included_definitions = []
        for definition in definitions:
            if definition in extension_tables:
                included_definitions.append(definition)
            else:
                # ignore exception for broken directives
                # raise Exception("definition {} specified but does not exist".format(definition))
                continue

    exclude_definitions = args.get('exclude_definitions')
    if exclude_definitions:
        for definition in exclude_definitions:
            if definition not in included_definitions:
                # ignore exception for broken directives
                # raise Exception("definition {} specified to exclude but does not exist".format(definition))
                continue
            included_definitions.remove(definition)

    if not included_definitions:
        # ignore exception for empty directives
        # raise Exception("Directive does not choose any definitions to show")
        return

    list_items = []
    for definition in included_definitions:
        href = url_for("extension_reference", lang=lang, slug=slug, version=version) + "#" + definition
        list_items.append(E.LI(E.A(definition, E.I(E.CLASS("fas fa-external-link-alt ml-2 small-icon")), href=href)))

    replacement = E.BLOCKQUOTE(E.CLASS("blockquote"), E.UL(E.CLASS("list-unstyled"), *list_items))
    pre_block.getparent().replace(pre_block, replacement)


def process_extensiontable(lines):
    args = {}
    for line in lines:
        if get_directive_arg(line, 'extension'):
            continue
        definitions = get_directive_arg(line, 'definitions')
        if definitions is not None:
            args['definitions'] = definitions.strip().split()
            continue
        exclude_definitions = get_directive_arg(line, 'exclude_definitions')
        if exclude_definitions is not None:
            args['exclude_definitions'] = exclude_definitions.strip().split()
            continue
        raise NotImplementedError(line)
    return args


def replace_codelist_directive(pre_block, directive_lines, lang, slug, version):
    if not directive_lines[0].strip() in ('.. csv-table-no-translate::', '.. csv-table::'):
        return False
    args = process_codelist(directive_lines[1:])
    codelist = args.get("codelist")

    href = url_for("extension_codelists", lang=lang, slug=slug, version=version) + "#" + codelist
    codelist_link = E.A(codelist, E.I(E.CLASS("fas fa-external-link-alt ml-2 small-icon")), href=href)

    pre_block.getparent().replace(pre_block, E.BLOCKQUOTE(E.CLASS("blockquote"), codelist_link))


def process_codelist(lines):
    args = {}
    for line in lines:
        if get_directive_arg(line, 'header-rows'):
            continue
        file_path = get_directive_arg(line, 'file')
        if file_path is not None:
            args['codelist'] = file_path.split("/")[-1]
            continue
        raise NotImplementedError(line)
    return args
