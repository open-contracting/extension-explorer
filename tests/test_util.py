import lxml.html
import pytest

from extension_explorer.util import (mark_headings,
                                     extensiontable_replacement, csv_table_replacement, get_directive_name,
                                     get_directive_options)

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


@pytest.mark.xfail
def test_get_extension_tables():
    pass


@pytest.mark.xfail
def test_gather_fields():
    pass


def test_mark_headings():
    html = """<div>
    <h1>A heading</h1>
    Text
    <h6>A heading</h6>
    Text
    <h2>A heading</h2>
    Text
    <h3>Another heading</h3>
    Text
    <h4>A heading</h4>
    </div>
    """

    html, headings = mark_headings(html)

    assert headings == [
        {'id': 'a-heading', 'level': 1, 'text': 'A heading'},
        {'id': 'a-heading-1', 'level': 2, 'text': 'A heading'},
        {'id': 'another-heading', 'level': 3, 'text': 'Another heading'},
        {'id': 'a-heading-2', 'level': 4, 'text': 'A heading'},
    ]

    assert html == """<div>
    <h1 id="a-heading">A heading</h1>
    Text
    <h6>A heading</h6>
    Text
    <h2 id="a-heading-1">A heading</h2>
    Text
    <h3 id="another-heading">Another heading</h3>
    Text
    <h4 id="a-heading-2">A heading</h4>
    </div>
    """


@pytest.mark.xfail
def test_highlight_json():
    pass


@pytest.mark.xfail
def test_replace_directives():
    pass


def test_extensiontable_replacement():
    extensiontable = """
    .. extensiontable::
    """.strip().split('\n')

    replacement = extensiontable_replacement(extensiontable, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#foo">foo<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#baz">baz<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_extensiontable_replacement_whitelist():
    extensiontable_whitelist = """
    .. extensiontable::
       :definitions: foo bar unknown
    """.strip().split('\n')

    replacement = extensiontable_replacement(extensiontable_whitelist, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#foo">foo<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
            '<li><a href="url/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_extensiontable_replacement_blacklist():
    extensiontable_blacklist = """
    .. extensiontable::
       :exclude_definitions: foo bar unknown
    """.strip().split('\n')

    replacement = extensiontable_replacement(extensiontable_blacklist, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#baz">baz<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_extensiontable_replacement_whitelist_blacklist():
    extensiontable_whitelist_blacklist = """
    .. extensiontable::
       :definitions: foo bar
       :exclude_definitions: foo
    """.strip().split('\n')

    replacement = extensiontable_replacement(extensiontable_whitelist_blacklist, 'url/path', definitions)

    assert lxml.html.tostring(replacement).decode() == \
    '<blockquote class="blockquote">' \
        '<ul class="list-unstyled">' \
            '<li><a href="url/path#bar">bar<i class="fas fa-external-link-alt ml-2 small-icon"></i></a></li>' \
        '</ul>' \
    '</blockquote>'  # noqa


def test_extensiontable_replacement_exclude_all():
    extensiontable_exclude_all = """
    .. extensiontable::
       :definitions: foo bar baz
       :exclude_definitions: foo bar baz
    """.strip().split('\n')

    replacement = extensiontable_replacement(extensiontable_exclude_all, 'url/path', definitions)

    assert replacement is None


def test_csv_table_replacement():
    replacement = csv_table_replacement(csv_table, 'url/path')

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
