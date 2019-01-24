# Extension Explorer

[![Build Status](https://secure.travis-ci.org/open-contracting/extension-explorer.png)](https://travis-ci.org/open-contracting/extension-explorer)
[![Coverage Status](https://coveralls.io/repos/open-contracting/extension-explorer/badge.png)](https://coveralls.io/r/open-contracting/extension-explorer)

## Development

### Get extensions data

Get a copy of extensions' translations:

```shell
git clone git@github.com:open-contracting/ocds-extensions-translations.git
```

Generate the data file, substituting the path to the above repository's `locale` directory for `path/to/locale`:

```
ocdsextensionregistry generate-data-file --locale-dir path/to/locale > extension_explorer/data/extensions.json
```

If you prefer to store the data file in another location, set the `EXTENSION_EXPLORER_DATA_FILENAME` environment variable to it.

### Stylesheets

Don't edit `extension_explorer/static/css/theme.css`. Instead, edit the files under `extension_explorer/static/lib` and run:

    pysassc extension_explorer/static/lib/scss/theme.scss > extension_explorer/static/css/theme.css

### Translations

If translatable strings are changed, change into the app's directory:

```shell
cd extension_explorer
```

Extract messages:

```shell
pybabel extract -F babel.cfg -o messages.pot .
```

Push to Transifex (`tx push -s`), translate, pull From Transifex (`tx pull -a`), then compile messages:

```shell
pybabel compile -d translations -f
```

If adding a new language, update `LANGS` in `views.py`.

### Run in development

```
FLASK_ENV=development FLASK_APP=extension_explorer/views.py flask run
```

Open <http://127.0.0.1:5000>

### Create static site

Create a static site in `extension_explorer/build`:

```shell
python freeze.py
```

Preview the static site:

```shell
cd extension_explorer/build
python -m http.server
```

Open <http://localhost:8000>

### Manual tests

The automated tests provide full code coverage, but you might still want to check pages visually. Here are a few features to check:

* Schema
  * Markdown is rendered <https://extensions.open-contracting.org/en/extensions/lots/master/schema/#Lot.status>
  * Sub-fields are shown in tables <https://extensions.open-contracting.org/en/extensions/location/master/schema/#Location.geometry.type>
  * Undeprecated fields are indicated <https://extensions.open-contracting.org/en/extensions/milestone_documents/master/schema/>
  * Removed fields are listed, grouped by deprecation <https://extensions.open-contracting.org/en/extensions/ppp/master/schema/#removed-fields>
  * Types include links to definitions in the extensions or in the standard <https://extensions.open-contracting.org/en/extensions/location/master/schema/>
  * Types of arrays indicate the types of items <https://extensions.open-contracting.org/en/extensions/location/master/schema/#Location.geometry.coordinates>
* Codelists
  * Additional columns are shown <https://extensions.open-contracting.org/en/extensions/ppp/master/codelists/#documentType.csv>
  * URLs are hyperlinked <https://extensions.open-contracting.org/en/extensions/location/master/codelists/#geometryType.csv>
  * Subtracted codes are shown <https://extensions.open-contracting.org/en/extensions/ppp/master/codelists/#-partyRole.csv>

## Maintenance

To update the requirements, delete and re-create the virtual environment, then run:

```shell
pip install -r requirements.in
pip freeze > requirements.txt
```
