import commonmark
from babel.core import UnknownLocaleError
from flask import Flask, abort, redirect, request, url_for
from flask import render_template
from flask_babel import Babel
from flask_env import MetaFlaskEnv
from werkzeug.exceptions import NotFound

from .util import (get_schema_tables, identify_headings, highlight_json, get_collections, get_extensions,
                   get_extension_and_version)
from .compat import replace_directives

LANGS = {
    'en': 'English',
    'es': 'Español',
    'fr': 'Français',
    'it': 'Italiano',
}


class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX = 'FLASK_'


app = Flask(__name__)
app.config.from_object(Configuration)
babel = Babel(app)


@app.context_processor
def inject_language_variables():
    def change_lang_in_url(lang):
        new_view_args = request.view_args.copy()
        new_view_args['lang'] = lang
        return url_for(request.endpoint, **new_view_args)
    return dict(change_lang_in_url=change_lang_in_url, langs=LANGS)


@babel.localeselector
def get_locale():
    return request.view_args.get('lang') or 'en'


@app.errorhandler(UnknownLocaleError)
def handle_unknown_locale_error(error):
    return NotFound()


@app.route('/')
def home():
    return redirect(url_for('lang_home', lang='en'))


@app.route('/<lang>/')
def lang_home(lang):
    return render_template('home.html', lang=lang)


@app.route('/<lang>/collections/')
def collections(lang):
    collections = get_collections()

    return render_template('collections.html', lang=lang, collections=collections)


@app.route('/<lang>/collection/<slug>/')
def collection(lang, slug):
    try:
        collection = next(collection for collection in get_collections() if collection['slug'] == slug)
    except StopIteration:
        abort(404)

    return render_template('collection.html', lang=lang, slug=slug, collection=collection)


@app.route('/<lang>/extensions/')
def extensions(lang):
    extensions = get_extensions().values()

    return render_template('extensions.html', lang=lang, extensions=extensions)


@app.route('/<lang>/extensions/<slug>/<version>/')
def extension(lang, slug, version):
    try:
        extension, extension_version = get_extension_and_version(slug, version)
    except KeyError:
        abort(404)

    tables = get_schema_tables(extension_version, lang)

    # Note: `readme` may contain unsafe HTML and JavaScript.
    schema_url = url_for('extension_schema', lang=lang, slug=slug, version=version)
    codelist_url = url_for('extension_codelists', lang=lang, slug=slug, version=version)
    readme = extension_version.get('readme', {}).get(lang, {})
    readme_html = commonmark.commonmark(readme)
    readme_html, headings = identify_headings(readme_html)
    readme_html = replace_directives(readme_html, schema_url, codelist_url, tables)
    readme_html, highlight_css = highlight_json(readme_html)

    return render_template('extension.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version, readme_html=readme_html, headings=headings,
                           highlight_css=highlight_css)


@app.route('/<lang>/extensions/<slug>/<version>/info/')
def extension_info(lang, slug, version):
    try:
        extension, extension_version = get_extension_and_version(slug, version)
    except KeyError:
        abort(404)

    return render_template('extension_info.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version)


@app.route('/<lang>/extensions/<slug>/<version>/schema/')
def extension_schema(lang, slug, version):
    try:
        extension, extension_version = get_extension_and_version(slug, version)
    except KeyError:
        abort(404)

    tables = get_schema_tables(extension_version, lang)

    return render_template('extension_schema.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version, tables=tables)


@app.route('/<lang>/extensions/<slug>/<version>/codelists/')
def extension_codelists(lang, slug, version):
    try:
        extension, extension_version = get_extension_and_version(slug, version)
    except KeyError:
        abort(404)

    return render_template('extension_codelists.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version)
