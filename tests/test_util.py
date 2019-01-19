from collections import OrderedDict
from copy import deepcopy

import pytest
from commonmark import commonmark

from extension_explorer.util import (get_extensions, set_tags, get_present_and_historical_versions, get_schema_tables,
                                     get_codelist_tables, identify_headings, highlight_json)

extension_version_template = {
    "schemas": {
        "release-schema.json": {
            "en": {}
        }
    },
    "codelists": {
        "codelist.csv": {
            "en": {}
        }
    }
}

release_schema = {
    "properties": {
        "empty": {
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
                            "description": "*Subsubfield*"
                        }
                    }
                }
            }
        },
        "undeprecated": {
            "deprecated": None
        },
        "deprecated": {
            "title": "Deprecated",
            "description": "Description",
            "type": "string",
            "deprecated": {
                "description": "Field has been deprecated because **reasons**.",
                "deprecatedVersion": "1.1"
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

codelist = {
    "fieldnames": [
        "Extra",
        "Description_en",
        "Title_en",
        "Code"
    ],
    "rows": [
        {
            "Code": "A code",
            "Title_en": "A title",
            "Description_en": "A description",
            "Extra": "An extra"
        },
        {
            "Code": "",
            "Title_en": "",
            "Description_en": "",
            "Extra": ""
        }
    ]
}

codelist_translated = {
    "fieldnames": [
        "Extra",
        "Descripción",
        "Título",
        "Código"
    ],
    "rows": [
        {
            "Código": "Un código",
            "Título": "Un título",
            "Descripción": "Un descripción",
            "Extra": "Un extra"
        },
        {
            "Código": "",
            "Título": "",
            "Descripción": "",
            "Extra": ""
        }
    ]
}


def test_set_tags():
    extensions = get_extensions()
    tags = set_tags(extensions)

    assert tags == (
        {'ppp': 'Public Private Partnerships'},
        {},
        {'open-contracting-extensions': 'open-contracting-extensions'},
    )


def test_get_present_and_historical_versions():
    present_versions, historical_versions = get_present_and_historical_versions({
        "latest_version": "master",
        "versions": {
            "master": {
                "version": "master",
                "date": ""
            },
            "v1.1": {
                "version": "v1.1",
                "date": "2017-05-09"
            },
            "v1.1.3": {
                "version": "v1.1.3",
                "date": "2018-02-01"
            },
            "v1.1.1": {
                "version": "v1.1.1",
                "date": "2017-08-07"
            }
        }
    })

    assert present_versions == [('master', 'latest'), ('v1.1.3', '2018-02-01')]
    assert historical_versions == [('v1.1.1', '2017-08-07'), ('v1.1', '2017-05-09')]


def test_get_present_and_historical_versions_master():
    present_versions, historical_versions = get_present_and_historical_versions({
        "latest_version": "master",
        "versions": {
            "master": {
                "version": "master",
                "date": ""
            }
        }
    })

    assert present_versions == [('master', 'latest')]
    assert historical_versions == []


def test_get_present_and_historical_versions_live():
    present_versions, historical_versions = get_present_and_historical_versions({
        "latest_version": "master",
        "versions": {
            "master": {
                "version": "master",
                "date": ""
            },
            "live": {
                "version": "live",
                "date": ""
            }
        }
    })

    assert present_versions == [('master', 'latest')]
    assert historical_versions == [('live', '')]


def test_get_schema_tables():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = release_schema

    tables = get_schema_tables(extension_version, 'en')

    assert dict(tables) == {
        'Asset': [
            ['field', 'Title', '<p>Description</p>\n', ['string', 'integer']],
        ],
        'Release': [
            ['empty', '', '', ['string']],
            ['array', 'Array', '', ['array of strings / integers']],
            ['ref', 'Asset', '', ['<a href="#asset">Asset</a> object']],
            ['refArray', 'Assets', '', ['array of <a href="#asset">Asset</a> objects']],
            ['null', 'Null', '', []],
            ['external', 'External', '', ['<a href="http://standard.open-contracting.org/1.1/en/schema/reference/#value">Value</a> object']],  # noqa
            ['field', 'Field', '', ['object']],
            ['field/subfield', '', '<p>Subfield</p>\n', ['object']],
            ['field/subfield/subsubfield', '', '<p><em>Subsubfield</em></p>\n', []],
            ['undeprecated', '', '<p><em>Undeprecated</em></p>\n', []],
            ['deprecated', 'Deprecated', '<p>Description</p>\n<p><em>Deprecated in OCDS 1.1: Field has been deprecated because <strong>reasons</strong>.</em></p>\n', ['string']],  # noqa
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
            ['nullArray', 'Array', '', ['array of strings']],
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


def test_get_codelist_tables():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists']['codelist.csv']['en'] = codelist

    tables = get_codelist_tables(extension_version, 'en')

    assert tables == [
        [
            'codelist.csv',
            ['Code', 'Title_en', 'Description_en'],
            [
                {
                    'code': 'A code',
                    'title': 'A title',
                    'content': {
                        'description': '<p>A description</p>\n',
                        'attributes': OrderedDict([('Extra', 'An extra')]),
                    },
                }, {
                    'code': '',
                    'title': '',
                    'content': {
                        'description': '',
                    },
                },
            ],
        ],
    ]


def test_get_codelist_tables_translation():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists']['codelist.csv']['en'] = codelist
    extension_version['codelists']['codelist.csv']['es'] = codelist_translated

    tables = get_codelist_tables(extension_version, 'es')

    assert tables == [
        [
            'codelist.csv',
            ['Código', 'Título', 'Descripción'],
            [
                {
                    'code': 'Un código',
                    'title': 'Un título',
                    'content': {
                        'description': '<p>Un descripción</p>\n',
                        'attributes': OrderedDict([('Extra', 'Un extra')]),
                    },
                }, {
                    'code': '',
                    'title': '',
                    'content': {
                        'description': '',
                    },
                },
            ],
        ],
    ]


def test_get_codelist_tables_subtrahend():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists'] = {
        "-codelist.csv": {
            "en": {
                "fieldnames": ["Code"],
                "rows": [{"Code": "A code"}]
            }
        }
    }

    tables = get_codelist_tables(extension_version, 'en')

    assert tables == [
        ['-codelist.csv', ['Code'], [{'code': 'A code'}]],
    ]


def test_get_codelist_tables_attributes():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists'] = {
        "codelist.csv": {
            "en": {
                "fieldnames": ["Extra"],
                "rows": [{"Extra": "An extra"}]
            }
        }
    }

    tables = get_codelist_tables(extension_version, 'en')

    assert tables == [
        ['codelist.csv', ['Description'], [{'content': {'attributes': OrderedDict([('Extra', 'An extra')])}}]],
    ]


def test_identify_headings():
    html = commonmark('# A heading\nText\n###### A heading\nText\n## A heading\nText\n### Another heading\nText\n#### Changelog\nText\n##### v1.0.0\nText\n#### A heading\nText\n')  # noqa

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
    html = commonmark('## Example\n```json\n{\n    "key": 1\n}\n```\n')

    html, css = highlight_json(html)

    assert html == """<div><h2>Example</h2>
<div class="highlight"><pre><span></span><span class="p">{</span>
    <span class="nt">"key"</span><span class="p">:</span> <span class="mi">1</span>
<span class="p">}</span>
</pre></div>
</div>"""

    assert css.startswith('.highlight .hll {')
