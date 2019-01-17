from copy import deepcopy

import commonmark
import pytest

from extension_explorer.util import get_schema_tables, identify_headings, highlight_json

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
        "external": {
            "title": "External",
            "type": "string",
            "$ref": "#/definitions/Value"
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
            ['field', 'Title', 'Description', 'string or integer'],
        ],
        'Release': [
            ['array', 'Array', '', 'array of strings / integers'],
            ['ref', 'Asset', '', '<a href="#asset">Asset</a> object'],
            ['refArray', 'Assets', '', 'array of <a href="#asset">Asset</a> objects'],
            ['null', 'Null', '', ''],
            ['external', 'External', '', '<a href="http://standard.open-contracting.org/1.1/en/schema/reference/#value">Value</a> object'],  # noqa
            ['field', 'Field', '', 'object'],
            ['field/subfield', '', 'Subfield', 'object'],
            ['field/subfield/subsubfield', '', 'Subsubfield', ''],
        ],
    }


def test_get_schema_tables_mixed_array_success():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = {
        "properties": {
            "nullArray": {
                "title": "Array",
                "type": [
                    "array",
                    "null"
                ],
                "items": {
                    "type": "string"
                }
            }
        }
    }

    tables = get_schema_tables(extension_version, 'en')

    assert dict(tables) == {
        'Release': [
            ['nullArray', 'Array', '', 'array of strings'],
        ]
    }


def test_get_schema_tables_mixed_array_failure():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = {
        "properties": {
            "mixedArray": {
                "title": "Array",
                "type": [
                    "array",
                    "string"
                ],
                "items": {
                    "title": "String",
                    "type": "string"
                }
            }
        }
    }

    with pytest.raises(NotImplementedError) as excinfo:
        get_schema_tables(extension_version, 'en')

    assert str(excinfo.value) == 'array / string is not implemented'


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

    assert str(excinfo.value) == 'array of objects with properties is not implemented'


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

    assert str(excinfo.value) == 'array of arrays with items is not implemented'


def test_identify_headings():
    html = commonmark.commonmark('# A heading\nText\n###### A heading\nText\n## A heading\nText\n### Another heading\nText\n#### Changelog\nText\n##### v1.0.0\nText\n#### A heading\nText\n')  # noqa

    html, headings = identify_headings(html)

    assert headings == [
        {'id': 'a-heading', 'level': 1, 'text': 'A heading'},
        {'id': 'a-heading-1', 'level': 2, 'text': 'A heading'},
        {'id': 'a-heading-2', 'level': 2, 'text': 'A heading'},
        {'id': 'another-heading', 'level': 3, 'text': 'Another heading'},
        {'id': 'changelog', 'level': 4, 'text': 'Changelog'},
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
<h4 id="changelog">Changelog</h4>
<p>Text</p>
<h5>v1.0.0</h5>
<p>Text</p>
<h4 id="a-heading-3">A heading</h4>
<p>Text</p>
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
