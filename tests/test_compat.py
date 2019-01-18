import lxml.html
import pytest
from commonmark import commonmark

from extension_explorer.compat import (replace_directives, get_extensiontable_replacement, get_csv_table_replacement,
                                       get_directive_name, get_directive_options)


invalid_directive = """
csv-table
   content
""".strip().split('\n')

csv_table = """
.. csv-table::
   :header-rows: 1
   :file: test.csv
""".strip().split('\n')

definitions = {
    'foo': 1,
    'bar': 1,
    'baz': 1,
}


def test_replace_directives():
    html = commonmark('```eval_rst\n.. extensiontable::\n```\n```eval_rst\n.. csv-table::\n   :file: test.csv\n```\n')

    html = replace_directives(html, 'schema/path', 'codelist/path', definitions)

    assert html == \
    '<div>' \
        '<blockquote class="blockquote">' \
            '<ul class="list-unstyled">' \
                '<li><a href="schema/path#foo">foo<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
                '<li><a href="schema/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
                '<li><a href="schema/path#baz">baz<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '</ul>' \
        '</blockquote>' \
        '<blockquote class="blockquote">' \
            '<a href="codelist/path#test.csv">test.csv<i class="fas fa-external-link-alt ml-2 small-icon"></i></a>' \
        '</blockquote>' \
    '</div>'  # noqa


def test_replace_directives_exclude_all():
    html = commonmark('Foo\n```eval_rst\n.. extensiontable::\n   :exclude_definitions: foo bar baz\n```\n')

    html = replace_directives(html, 'schema/path', 'codelist/path', definitions)

    assert html == '<div><p>Foo</p>\n</div>'


def test_replace_directives_unknown_directive():
    html = commonmark('```eval_rst\n.. directive::\n```\n')

    with pytest.raises(NotImplementedError) as excinfo:
        replace_directives(html, 'schema/path', 'codelist/path', definitions)

    assert str(excinfo.value) == 'Unknown directive: directive'


def test_replace_directives_unexpected_line():
    html = commonmark('```eval_rst\ncontent\n```\n')

    with pytest.raises(NotImplementedError) as excinfo:
        replace_directives(html, 'schema/path', 'codelist/path', definitions)

    assert str(excinfo.value) == 'Unexpected line: content'


def test_get_extensiontable_replacement():
    extensiontable = """
    .. extensiontable::
    """.strip().split('\n')

    replacement = get_extensiontable_replacement(extensiontable, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#foo">foo<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#baz">baz<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_get_extensiontable_replacement_whitelist():
    extensiontable_whitelist = """
    .. extensiontable::
       :definitions: foo bar unknown
    """.strip().split('\n')

    replacement = get_extensiontable_replacement(extensiontable_whitelist, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#foo">foo<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_get_extensiontable_replacement_blacklist():
    extensiontable_blacklist = """
    .. extensiontable::
       :exclude_definitions: foo bar unknown
    """.strip().split('\n')

    replacement = get_extensiontable_replacement(extensiontable_blacklist, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#baz">baz<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_get_extensiontable_replacement_exclude_all():
    extensiontable_exclude_all = """
    .. extensiontable::
       :exclude_definitions: foo bar baz
    """.strip().split('\n')

    replacement = get_extensiontable_replacement(extensiontable_exclude_all, 'url/path', definitions)

    assert replacement is None


def test_get_csv_table_replacement():
    replacement = get_csv_table_replacement(csv_table, 'url/path')

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<a href="url/path#test.csv">test.csv<i class="fas fa-external-link-alt ml-2 small-icon"></i></a>' \
    '</blockquote>'  # noqa


def test_get_directive_name():
    directive_name = get_directive_name(csv_table)

    assert directive_name == 'csv-table'


def test_get_directive_name_invalid():
    directive_name = get_directive_name(invalid_directive)

    assert directive_name is None


def test_get_directive_options():
    directive_options = get_directive_options(csv_table, ['file', 'header-rows'])

    assert directive_options == {'file': 'test.csv', 'header-rows': '1'}


def test_get_directive_options_unknown_option():
    with pytest.raises(NotImplementedError) as excinfo:
        get_directive_options(csv_table, ['file'])

    assert str(excinfo.value) == 'Unknown option: header-rows'


def test_get_directive_options_unexpected_line():
    with pytest.raises(NotImplementedError) as excinfo:
        get_directive_options(invalid_directive)

    assert str(excinfo.value) == 'Unexpected line: content'
