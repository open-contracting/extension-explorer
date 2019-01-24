import re

from babel.core import UnknownLocaleError
from flask import Flask, abort, render_template, request, send_file, url_for
from flask_babel import Babel, gettext
from flask_env import MetaFlaskEnv
from werkzeug.exceptions import NotFound

from .util import (get_extension_explorer_data_filename, get_extensions, set_tags, get_extension_and_version,
                   get_present_and_historical_versions, identify_headings, highlight_json, get_removed_fields,
                   get_schema_tables, get_codelist_tables, commonmark)
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
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
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


@app.route('/extensions.json')
def extensions_json():
    # Used by extensionexplorerlinklist in sphinxcontrib-opencontracting.
    return send_file(get_extension_explorer_data_filename())


@app.route('/')
def home():
    title = gettext('OCDS Extension Explorer')
    url = url_for('lang_home', lang='en')

    return render_template('redirect.html', title=title, redirect=url)


@app.route('/<lang>/')
def lang_home(lang):
    return render_template('home.html', lang=lang)


@app.route('/<lang>/documentation/')
def documentation(lang):
    return render_template('documentation.html', lang=lang)


@app.route('/<lang>/extensions/')
def extensions(lang):
    extensions = get_extensions()
    profiles, topics, publishers = set_tags(extensions)

    return render_template('extensions.html', lang=lang, extensions=extensions.values(), profiles=profiles,
                           topics=topics, publishers=publishers)


@app.route('/<lang>/extensions/<identifier>/')
def extension(lang, identifier):
    try:
        extension = get_extensions()[identifier]
    except KeyError:
        abort(404)

    title = gettext('%(name)s — OCDS Extension Explorer', name=extension['name'][lang])
    url = url_for('extension_documentation', lang=lang, identifier=identifier, version=extension['latest_version'])

    return render_template('redirect.html', title=title, redirect=url)


@app.route('/<lang>/extensions/<identifier>/<version>/')
def extension_documentation(lang, identifier, version):
    try:
        extension, extension_version = get_extension_and_version(identifier, version)
    except KeyError:
        abort(404)

    present_versions, historical_versions = get_present_and_historical_versions(extension)
    tables = get_schema_tables(extension_version, lang)

    # Note: `readme` may contain unsafe HTML and JavaScript.
    schema_url = url_for('extension_schema', lang=lang, identifier=identifier, version=version)
    codelist_url = url_for('extension_codelists', lang=lang, identifier=identifier, version=version)
    readme = extension_version.get('readme', {}).get(lang, {})
    # Remove the first heading.
    readme = re.sub(r'\A# [^\n]+', '', readme)
    readme_html = commonmark(readme)
    readme_html, headings = identify_headings(readme_html)
    readme_html = replace_directives(readme_html, schema_url, codelist_url, tables)
    readme_html, highlight_css = highlight_json(readme_html)

    return render_template('extension_documentation.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, readme_html=readme_html, headings=headings,
                           highlight_css=highlight_css)


@app.route('/<lang>/extensions/<identifier>/<version>/schema/')
def extension_schema(lang, identifier, version):
    try:
        extension, extension_version = get_extension_and_version(identifier, version)
    except KeyError:
        abort(404)

    present_versions, historical_versions = get_present_and_historical_versions(extension)
    tables = get_schema_tables(extension_version, lang)
    removed_fields = get_removed_fields(extension_version, lang)

    return render_template('extension_schema.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, tables=tables, removed_fields=removed_fields)


@app.route('/<lang>/extensions/<identifier>/<version>/codelists/')
def extension_codelists(lang, identifier, version):
    try:
        extension, extension_version = get_extension_and_version(identifier, version)
    except KeyError:
        abort(404)

    present_versions, historical_versions = get_present_and_historical_versions(extension)
    tables = get_codelist_tables(extension_version, lang)

    return render_template('extension_codelists.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, tables=tables)
