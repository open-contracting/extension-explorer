# Extension Explorer

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

If you prefer to store the data file in another location, set the `EXTENSION_EXPLORER_DATA_FILENAME` environment variable.

### Stylesheets

Don't edit `extension_explorer/static/css`. Instead, edit `extension_explorer/static/lib` and run:

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

Push to Transifex:

```shell
tx push -s
```

Translate, then pull From Transifex:

```shell
tx pull -a
```

Finally, compile messages:

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
python -m http.server --directory extension_explorer/build
```

Open <http://localhost:8000>

### Manual tests

The automated tests provide full code coverage, but you might still want to check pages visually. Here are a few features to check:

* Documentation
  * The `list-table` Sphinx directive is rendered <https://extensions.open-contracting.org/en/extensions/budget_project/master/#guidance>
  * The `extensiontable` Sphinx directive is linked <https://extensions.open-contracting.org/en/extensions/lots/v1.1.3/#schema>
* Schema
  * Paragraphs include links to existing definitions from:
    * the standard <https://extensions.open-contracting.org/en/extensions/additionalContactPoint/master/schema/#organization>
    * other extensions <https://extensions.open-contracting.org/en/extensions/ppp/master/schema/>
  * The following fields are shown in tables:
    * Sub-fields <https://extensions.open-contracting.org/en/extensions/location/master/schema/#Location.geometry.type>
    * Pattern properties <https://extensions.open-contracting.org/en/extensions/metrics/master/schema/#Observation.dimensions.(^.*)>
  * The "Description" column:
    * renders Markdown <https://extensions.open-contracting.org/en/extensions/lots/master/schema/#Lot.status>
    * displays deprecation message
    * indicates whether undeprecated <https://extensions.open-contracting.org/en/extensions/milestone_documents/master/schema/#Milestone.documents>
    * indicates multilingual support <https://extensions.open-contracting.org/en/extensions/budget_project/master/schema/#Project.title>
    * indicates whether it overrides:
      * the standard <https://extensions.open-contracting.org/en/extensions/ppp/master/schema/#.tag>
      * other extensions <https://extensions.open-contracting.org/en/extensions/ppp/master/schema/#Metric.id>
  * The "Types" column includes links to definitions within the extensions and to:
    * the standard <https://extensions.open-contracting.org/en/extensions/location/master/schema/>
    * other extensions <https://extensions.open-contracting.org/en/extensions/transaction_milestones/master/schema/>
  * Types of arrays indicate the types of items <https://extensions.open-contracting.org/en/extensions/location/master/schema/#Location.geometry.coordinates>
  * Removed fields are listed, grouped by deprecation <https://extensions.open-contracting.org/en/extensions/ppp/master/schema/#removed-fields>
* Codelists
  * Additional columns are shown <https://extensions.open-contracting.org/en/extensions/ppp/master/codelists/#documentType.csv>
  * URLs are hyperlinked <https://extensions.open-contracting.org/en/extensions/location/master/codelists/#geometryType.csv>
  * Subtracted codes are shown <https://extensions.open-contracting.org/en/extensions/ppp/master/codelists/#-partyRole.csv>
  * Added, removed, and replaced codelists link to original codelists <https://extensions.open-contracting.org/en/extensions/ppp/master/codelists/>

Note: No extension deprecates codes, so code deprecation isn't implemented yet.

## Maintenance

To update the requirements, delete and re-create the virtual environment, then run:

```shell
pip install -r requirements.in
pip freeze > requirements.txt
```
