# Website for exploring OCDS extensions.

# Install

Install dependencies:

```
$ python3 -m venv .ve
$ source .ve/bin/activate
$ pip install -r requirements.txt
```

# Get data

You need the data from https://github.com/open-contracting/extensions-data-collector

Get this repository, and run it as directed in the readme.

Copy the resulting JSON data file to extension_explorer/data.json
(You can also copy the file to your own location and set the EXTENSION_EXPLORER_DATA_FILE environment variable.)


# Run in dev

Flask in development mode
```
FLASK_ENV=development FLASK_APP=extension_explorer/views.py flask run
```

# I18n

## Compile messages:

This needs to be done on each computer for i18n to work. If updating messages from transifex this has to be done last.

```
cd extension_explorer
pybabel compile -d translations
```

## Extract messages and push to transifex
```
cd extension_explorer
pybabel extract -F .babel.cfg -o messages.pot

tx push --source
```

Commit this file to github

## Pull From Transifex

When new translations happen
```
tx pull --all
```
Commit new files to github


# Create static site

To create a "Frozen" site (it will appear in extension_explorer/build ):

```
python freeze.py
```

All the links in the website are absolute, so if you just open the file in a web browser none of the links will work. 
Instead, change to the extension_explorer/build directory and run:

    python -m http.server 8000

Check http://localhost:8000

# Tests

```
$ python -m pytest
```

## Updating requirements.


```
$ rm -rf venv .ve
$ python3 -m venv .ve
$ source .ve/bin/activate
$ pip install -r requirements.in
$ pip freeze > requirements.txt
$ grep awesome-slugify requirements.txt >> tmp; cat tmp >> requirements.txt; rm tmp
```

IMPORTANT: The last line of the above needs to run as awesome-slugify has to be installed after python-slugify.


