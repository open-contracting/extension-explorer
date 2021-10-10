import os

from flask import url_for

EMPTY_EXTENSIONS_JSON = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures', 'empty.json')


def test_extensions_json(client):
    response = client.get(url_for('extensions_json'))
    assert response.status_code == 200


def test_home(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200

    assert b"""<meta http-equiv="refresh" content="0;url='/en/'">""" in response.data


def test_lang_home(client):
    response = client.get(url_for('lang_home', lang='en'))
    assert response.status_code == 200


def test_publishers(client):
    response = client.get(url_for('publishers', lang='en'))
    assert response.status_code == 200


def test_users(client):
    response = client.get(url_for('users', lang='en'))
    assert response.status_code == 200


def test_extensions(client):
    response = client.get(url_for('extensions', lang='en'))
    assert response.status_code == 200


def test_extension(client):
    response = client.get(url_for('extension', lang='en', identifier='location'))
    assert response.status_code == 200

    assert b"""<meta http-equiv="refresh" content="0;url='/en/extensions/location/v1.1.3/'">""" in response.data


def test_extension_documentation(client):
    response = client.get(url_for('extension_documentation', lang='en', identifier='location', version='v1.1.3'))
    assert response.status_code == 200

    assert b'Location Data' not in response.data  # first header
    assert b'Communicating the location of proposed or executed contract delivery is important to ' in response.data


def test_extension_schema(client):
    response = client.get(url_for('extension_schema', lang='en', identifier='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_codelists(client):
    response = client.get(url_for('extension_codelists', lang='en', identifier='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_metadata_file(client):
    response = client.get(url_for('extension_metadata_file', lang='en', identifier='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_documentation_file(client):
    response = client.get(url_for('extension_documentation_file', lang='en', identifier='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_schema_file(client):
    response = client.get(url_for('extension_schema_file', lang='en', identifier='location', version='v1.1.3',
                                  filename='release-schema.json'))
    assert response.status_code == 200


def test_extension_codelist_file(client):
    response = client.get(url_for('extension_codelist_file', lang='en', identifier='location', version='v1.1.3',
                                  filename='geometryType.csv'))
    assert response.status_code == 200


def test_lang_home_404(client):
    response = client.get(url_for('lang_home', lang='nonexistent'))
    assert response.status_code == 404


def test_extension_404(client):
    response = client.get(url_for('extension', lang='en', identifier='nonexistent'))
    assert response.status_code == 404


def test_extension_documentation_404_extension(client):
    response = client.get(url_for('extension_documentation', lang='en', identifier='nonexistent', version='v1.1.3'))
    assert response.status_code == 404


def test_extension_schema_404_extension(client):
    response = client.get(url_for('extension_schema', lang='en', identifier='nonexistent', version='v1.1.3'))
    assert response.status_code == 404


def test_extension_codelists_404_extension(client):
    response = client.get(url_for('extension_codelists', lang='en', identifier='nonexistent', version='v1.1.3'))
    assert response.status_code == 404


def test_extension_documentation_404_version(client):
    response = client.get(url_for('extension_documentation', lang='en', identifier='location', version='nonexistent'))
    assert response.status_code == 404


def test_extension_schema_404_version(client):
    response = client.get(url_for('extension_schema', lang='en', identifier='location', version='nonexistent'))
    assert response.status_code == 404


def test_extension_codelists_404_version(client):
    response = client.get(url_for('extension_codelists', lang='en', identifier='location', version='nonexistent'))
    assert response.status_code == 404


def test_extension_schema_404_no_schema(client, monkeypatch):
    monkeypatch.setenv('EXTENSION_EXPLORER_DATA_FILENAME', EMPTY_EXTENSIONS_JSON)
    response = client.get(url_for('extension_documentation', lang='en', identifier='empty', version='master'))
    assert response.status_code == 200
    response = client.get(url_for('extension_schema', lang='en', identifier='empty', version='master'))
    assert response.status_code == 404


def test_extension_codelists_404_no_codelists(client, monkeypatch):
    monkeypatch.setenv('EXTENSION_EXPLORER_DATA_FILENAME', EMPTY_EXTENSIONS_JSON)
    response = client.get(url_for('extension_documentation', lang='en', identifier='empty', version='master'))
    assert response.status_code == 200
    response = client.get(url_for('extension_codelists', lang='en', identifier='empty', version='master'))
    assert response.status_code == 404
