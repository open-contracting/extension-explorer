import os

from flask import url_for

os.environ['EXTENSION_EXPLORER_DATA_FILE'] = os.path.join('tests', 'fixtures', 'data.json')


def test_home(client):
    response = client.get(url_for('home'))
    assert response.status_code == 302
    assert response.headers['Location'] == 'http://localhost/en/'


def test_lang_home(client):
    response = client.get(url_for('lang_home', lang='en'))
    assert response.status_code == 200


def test_extension(client):
    response = client.get(url_for('extension', lang='en', slug='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_schema(client):
    response = client.get(url_for('extension_schema', lang='en', slug='location', version='v1.1.3'))
    assert response.status_code == 200


def test_extension_codelists(client):
    response = client.get(url_for('extension_codelists', lang='en', slug='location', version='v1.1.3'))
    assert response.status_code == 200
