from copy import deepcopy

import commonmark
import pytest

from extension_explorer.util import get_schema_tables, mark_headings, highlight_json

extension_version_template = {
    "schemas": {
        "release-schema.json": {
            "en": {}
        }
    }
}

release_schema = {
    "properties": {
        "omit": {
            "type": "string"
        },
        "array": {
            "title": "Array",
            "type": "array",
            "items": {
                "type": [
                    "string",
                    "integer",
                    "null",
                    None
                ]
            }
        },
        "ref": {
            "title": "Asset",
            "type": "object",
            "$ref": "#/definitions/Asset"
        },
        "refArray": {
            "title": "Assets",
            "type": "array",
            "items": {
                "$ref": "#/definitions/Asset"
            }
        },
        "null": {
            "title": "Null",
            "type": [
                "null",
                None
            ]
        },
        "typeRef": {
            "title": "Type",
            "$ref": "#/definitions/Asset"
        },
        "field": {
            "title": "Field",
            "type": "object",
            "properties": {
                "subfield": {
                    "description": "Subfield",
                    "type": "object",
                    "properties": {
                        "subsubfield": {
                            "description": "Subsubfield"
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "Asset": {
            "type": "object",
            "properties": {
                "field": {
                    "title": "Title",
                    "description": "Description",
                    "type": [
                        "string",
                        "integer",
                        "null",
                        None
                    ]
                }
            }
        }
    }
}


def test_get_schema_tables():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = release_schema

    tables = get_schema_tables(extension_version, 'en')

    assert dict(tables) == {
        'Asset': [
            ['field', 'Title', 'Description', 'string, integer'],
        ],
        'Release': [
            ['array', 'Array', '', 'array (string, integer)'],
            ['ref', 'Asset', '', 'Asset'],
            ['refArray', 'Assets', '', 'array (Asset)'],
            ['null', 'Null', '', ''],
            ['typeRef', 'Type', '', 'Asset'],
            ['field', 'Field', '', 'object'],
            ['field/subfield', '', 'Subfield', 'object'],
            ['field/subfield/subsubfield', '', 'Subsubfield', ''],
        ],
    }


def test_get_schema_tables_object_array():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = {
        "properties": {
            "objectArray": {
                "title": "Array",
                "items": {
                    "title": "Object",
                    "properties": {
                        "field": {
                            "title": "Field"
                        }
                    }
                }
            }
        }
    }

    with pytest.raises(NotImplementedError) as excinfo:
        get_schema_tables(extension_version, 'en')

    assert str(excinfo.value) == 'arrays of objects with properties are not implemented'


def test_get_schema_tables_array_array():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = {
        "properties": {
            "arrayArray": {
                "title": "Array",
                "items": {
                    "title": "Array",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    }

    with pytest.raises(NotImplementedError) as excinfo:
        get_schema_tables(extension_version, 'en')

    assert str(excinfo.value) == 'arrays of arrays with items are not implemented'


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
