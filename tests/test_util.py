import pytest

from extension_explorer.util import get_extension_tables, mark_headings, highlight_json, gather_fields


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
    html = """<div>
    </div>
    """
