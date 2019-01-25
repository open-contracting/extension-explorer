from collections import OrderedDict
from copy import deepcopy

import pytest

from extension_explorer.util import (get_extensions, set_tags, get_present_and_historical_versions, identify_headings,
                                     highlight_json, get_removed_fields, get_schema_tables, get_codelist_tables,
                                     commonmark)

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
                        },
                        "subsubremoved": None
                    }
                },
                "subremoved": None
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
        },
        "removed": None
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
                },
                "removed": None
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

    assert extensions['location']['tags'] == {'recommended', 'profile-ppp', 'publisher-open-contracting-extensions'}


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


def test_get_removed_fields():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = release_schema

    fields = get_removed_fields(extension_version, 'en')

    assert fields == {
        'active': [
            {'definition_path': '', 'path': '.field.subfield.subsubremoved'},
            {'definition_path': '', 'path': '.field.subremoved'},
            {'definition_path': '', 'path': '.removed'},
            {'definition_path': 'Asset', 'path': '.removed'},
        ],
    }


def test_get_schema_tables():
    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = release_schema

    tables = get_schema_tables(extension_version, 'en')

    assert dict(tables) == {
        'Asset': [
            {
                'definition_path': 'Asset',
                'path': '.field',
                'schema': release_schema['definitions']['Asset']['properties']['field'],
                'multilingual': False,
                'title': 'Title',
                'description': '<p>Description</p>\n',
                'types': 'string or integer',
            },
        ],
        'Release': [
            {
                'definition_path': 'Release',
                'path': '.empty',
                'schema': release_schema['properties']['empty'],
                'multilingual': False,
                'title': '',
                'description': '',
                'types': 'string',
            },
            {
                'definition_path': 'Release',
                'path': '.array',
                'schema': release_schema['properties']['array'],
                'multilingual': False,
                'title': 'Array',
                'description': '',
                'types': 'array of strings / integers',
            },
            {
                'definition_path': 'Release',
                'path': '.ref',
                'schema': release_schema['properties']['ref'],
                'multilingual': False,
                'title': 'Asset',
                'description': '',
                'types': '<a href="#asset">Asset</a> object',
            },
            {
                'definition_path': 'Release',
                'path': '.refArray',
                'schema': release_schema['properties']['refArray'],
                'multilingual': False,
                'title': 'Assets',
                'description': '',
                'types': 'array of <a href="#asset">Asset</a> objects',
            },
            {
                'definition_path': 'Release',
                'path': '.null',
                'schema': release_schema['properties']['null'],
                'multilingual': False,
                'title': 'Null',
                'description': '',
                'types': '',
            },
            {
                'definition_path': 'Release',
                'path': '.external',
                'schema': release_schema['properties']['external'],
                'multilingual': False,
                'title': 'External',
                'description': '',
                'types': '<a href="http://standard.open-contracting.org/1.1/en/schema/reference/#value">Value</a> object',  # noqa
            },
            {
                'definition_path': 'Release',
                'path': '.field',
                'schema': release_schema['properties']['field'],
                'multilingual': False,
                'title': 'Field',
                'description': '',
                'types': 'object',
            },
            {
                'definition_path': 'Release',
                'path': '.field.subfield',
                'schema': release_schema['properties']['field']['properties']['subfield'],
                'multilingual': False,
                'title': '',
                'description': '<p>Subfield</p>\n',
                'types': 'object',
            },
            {
                'definition_path': 'Release',
                'path': '.field.subfield.subsubfield',
                'schema': release_schema['properties']['field']['properties']['subfield']['properties']['subsubfield'],  # noqa
                'multilingual': False,
                'title': '',
                'description': '<p><em>Subsubfield</em></p>\n',
                'types': '',
            },
            {
                'definition_path': 'Release',
                'path': '.undeprecated',
                'schema': release_schema['properties']['undeprecated'],
                'multilingual': False,
                'title': '',
                'description': '<p><em>Undeprecated</em></p>\n',
                'types': '',
            },
            {
                'definition_path': 'Release',
                'path': '.deprecated',
                'schema': release_schema['properties']['deprecated'],
                'multilingual': False,
                'title': 'Deprecated',
                'description': '<p>Description</p>\n<p><strong>Deprecated in OCDS 1.1</strong>: Field has been deprecated because <strong>reasons</strong>.</p>\n',  # noqa
                'types': 'string',
            },
        ],
    }


def test_get_schema_tables_mixed_array_success():
    schema = {
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

    extension_version = deepcopy(extension_version_template)
    extension_version['schemas']['release-schema.json']['en'] = schema

    tables = get_schema_tables(extension_version, 'en')

    assert dict(tables) == {
        'Release': [
            {
                'definition_path': 'Release',
                'path': '.nullArray',
                'schema': schema['properties']['nullArray'],
                'multilingual': False,
                'title': 'Array',
                'description': '',
                'types': 'array of strings',
            },
        ],
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

    assert str(excinfo.value).startswith('array of objects with properties is not implemented: ')


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

    assert str(excinfo.value).startswith('array of arrays with items is not implemented: ')


def test_get_codelist_tables():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists']['codelist.csv']['en'] = codelist

    tables = get_codelist_tables(extension_version, 'en')

    assert tables == [
        ['codelist.csv', 'codelist.csv', None, ['Code', 'Title_en', 'Description_en'], [
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
        ]],
    ]


def test_get_codelist_tables_translation():
    extension_version = deepcopy(extension_version_template)
    extension_version['codelists']['codelist.csv']['en'] = codelist
    extension_version['codelists']['codelist.csv']['es'] = codelist_translated

    tables = get_codelist_tables(extension_version, 'es')

    assert tables == [
        ['codelist.csv', 'codelist.csv', None, ['Código', 'Título', 'Descripción'], [
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
        ]],
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
        ['-codelist.csv', 'codelist.csv', None, ['Code'], [
            {'code': 'A code'},
        ]],
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
        ['codelist.csv', 'codelist.csv', None, ['Description'], [
            {'content': {'attributes': OrderedDict([('Extra', 'An extra')])}},
        ]],
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
