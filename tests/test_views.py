from flask import url_for


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


def test_documentation(client):
    response = client.get(url_for('documentation', lang='en'))
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
