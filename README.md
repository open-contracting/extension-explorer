### Website for exploring OCDS extensions.

Install dependencies:

```
$ python3 -m venv .ve
$ source .ve/bin/activate
$ pip install -r requirements.txt
```


Run:

Flask in development mode
```
FLASK_ENV=development FLASK_APP=extension_explorer/views.py flask run
```

Tests
```
$ python -m pytest
```