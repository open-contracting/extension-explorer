import commonmark
import pytest

from extension_explorer.util import get_extension_tables, mark_headings, highlight_json, gather_fields


@pytest.mark.xfail
def test_get_extension_tables():
    pass


@pytest.mark.xfail
def test_gather_fields():
    pass


def test_mark_headings():
    html = commonmark.commonmark('# A heading\nText\n###### A heading\nText\n## A heading\nText\n### Another heading\nText\n#### A heading\n')  # noqa

    html, headings = mark_headings(html)

    assert headings == [
        {'id': 'a-heading', 'level': 1, 'text': 'A heading'},
        {'id': 'a-heading-1', 'level': 6, 'text': 'A heading'},
        {'id': 'a-heading-2', 'level': 2, 'text': 'A heading'},
        {'id': 'another-heading', 'level': 3, 'text': 'Another heading'},
        {'id': 'a-heading-3', 'level': 4, 'text': 'A heading'},
    ]

    assert html == """<div><h1 id="a-heading">A heading</h1>
<p>Text</p>
<h6 id="a-heading-1">A heading</h6>
<p>Text</p>
<h2 id="a-heading-2">A heading</h2>
<p>Text</p>
<h3 id="another-heading">Another heading</h3>
<p>Text</p>
<h4 id="a-heading-3">A heading</h4>
</div>"""


def test_highlight_json():
    html = commonmark.commonmark('## Example\n```json\n{\n    "key": 1\n}\n```\n')

    html, css = highlight_json(html)

    assert html == """<div><h2>Example</h2>
<div class="highlight"><pre><span></span><span class="p">{</span>
    <span class="nt">"key"</span><span class="p">:</span> <span class="mi">1</span>
<span class="p">}</span>
</pre></div>
</div>"""

    assert css.startswith('.highlight .hll {')
