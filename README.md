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

# Modify the theme

Don't edit `extension_explorer/static/css/theme.css` directly. Instead, edit the files under `extension_explorer/static/lib`, then run:

    sassc extension_explorer/static/lib/scss/theme.scss > extension_explorer/static/css/theme.css

# Run in dev

Flask in development mode
```
FLASK_ENV=development FLASK_APP=extension_explorer/views.py flask run
```

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