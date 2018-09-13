### Website for exploring OCDS extensions.

Install dependencies:

```
$ python3 -m venv .ve
$ source .ve/bin/activate
$ pip install -r requirements.txt
```

Get data:

You need the data from https://github.com/open-contracting/extensions-data-collector

Get this repository, and run it as directed in the readme.

Copy the resulting JSON data file to extension_explorer/data.json
(You can also copy the file to your own location and set the EXTENSION_EXPLORER_DATA_FILE environment variable.)


Run:

Flask in development mode
```
FLASK_ENV=development FLASK_APP=extension_explorer/views.py flask run
```

Tests
```
$ python -m pytest
```