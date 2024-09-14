import csv
import re
from io import StringIO

from babel.core import UnknownLocaleError
from flask import Flask, abort, render_template, request, send_file, url_for
from flask_babel import Babel, gettext
from flask_env import MetaFlaskEnv
from werkzeug.exceptions import NotFound

from .util import (
    get_codelist_tables,
    get_extension_explorer_data_filename,
    get_extensions,
    get_present_and_historical_versions,
    get_removed_fields,
    get_schema_tables,
    highlight_json,
    identify_headings,
    markdown,
    set_tags,
)

LANGS = {
    'en': 'English',
    'es': 'Español',
}


class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX = 'FLASK_'
    FREEZER_IGNORE_404_NOT_FOUND = True
    FREEZER_STATIC_IGNORE = ('*.scss', 'LICENSE')


def get_locale():
    return request.view_args.get('lang') or 'en'


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.json.compact = False
app.json.sort_keys = False
app.config.from_object(Configuration)
babel = Babel(app, locale_selector=get_locale)


def get_extension(identifier):
    try:
        extensions = get_extensions(get_extension_explorer_data_filename())
        return extensions[identifier]
    except KeyError:
        abort(404)


def get_extension_and_version(identifier, version):
    try:
        extensions = get_extensions(get_extension_explorer_data_filename())
        # Always render a master branch, even if not present.
        default_master = version == 'master' and version not in extensions[identifier]['versions']
        if default_master:
            version = extensions[identifier]['latest_version']
        return extensions[identifier], extensions[identifier]['versions'][version], default_master
    except KeyError:
        abort(404)


@app.context_processor
def inject_language_variables():
    def change_lang_in_url(lang):
        new_view_args = request.view_args.copy()
        new_view_args['lang'] = lang
        return url_for(request.endpoint, **new_view_args)
    return {'change_lang_in_url': change_lang_in_url, 'langs': LANGS}


@app.errorhandler(UnknownLocaleError)
def handle_unknown_locale_error(error):
    return NotFound()


@app.route('/robots.txt')
def robots_txt():
    return 'User-Agent: *\nDisallow:\n'


@app.route('/extensions.json')
def extensions_json():
    # Used by extensionexplorerlinklist in sphinxcontrib-opencontracting.
    return send_file(get_extension_explorer_data_filename())


@app.route('/')
def home():
    title = gettext('OCDS Extension Explorer')
    url = url_for('lang_home', lang='en')

    return render_template('redirect.html', title=title, redirect=url, lang='en')


@app.route('/<lang>/')
def lang_home(lang):
    return render_template('home.html', lang=lang)


@app.route('/<lang>/publishers/')
def publishers(lang):
    return render_template('publishers.html', lang=lang)


@app.route('/<lang>/users/')
def users(lang):
    return render_template('users.html', lang=lang)


@app.route('/<lang>/extensions/')
def extensions(lang):
    extensions = get_extensions(get_extension_explorer_data_filename())

    profiles, topics, publishers = set_tags(extensions)

    return render_template('extensions.html', lang=lang, extensions=extensions.values(), profiles=profiles,
                           topics=topics, publishers=publishers)


@app.route('/<lang>/extensions/<identifier>/')
def extension(lang, identifier):
    extension = get_extension(identifier)

    title = gettext('%(name)s — OCDS Extension Explorer', name=extension['name'][lang])
    url = url_for('extension_documentation', lang=lang, identifier=identifier, version=extension['latest_version'])

    return render_template('redirect.html', title=title, redirect=url, lang=lang)


@app.route('/<lang>/extensions/<identifier>/<version>/')
def extension_documentation(lang, identifier, version):
    extension, extension_version, default_master = get_extension_and_version(identifier, version)

    present_versions, historical_versions = get_present_and_historical_versions(extension)

    # Note: `readme` may contain unsafe HTML and JavaScript.
    readme = extension_version.get('readme', {}).get(lang, {})
    # Remove the first heading.
    readme = re.sub(r'\A# [^\n]+', '', readme)
    readme_html = markdown(readme)
    readme_html, headings = identify_headings(readme_html)
    readme_html, highlight_css = highlight_json(readme_html)

    return render_template('extension_documentation.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, default_master=default_master,
                           readme_html=readme_html, headings=headings, highlight_css=highlight_css)


@app.route('/<lang>/extensions/<identifier>/<version>/schema/')
def extension_schema(lang, identifier, version):
    extension, extension_version, default_master = get_extension_and_version(identifier, version)
    if not extension_version['schemas']['release-schema.json'][lang]:
        abort(404)

    present_versions, historical_versions = get_present_and_historical_versions(extension)
    tables = get_schema_tables(extension_version, lang)
    removed_fields = get_removed_fields(extension_version, lang)

    return render_template('extension_schema.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, default_master=default_master, tables=tables,
                           removed_fields=removed_fields)


@app.route('/<lang>/extensions/<identifier>/<version>/codelists/')
def extension_codelists(lang, identifier, version):
    extension, extension_version, default_master = get_extension_and_version(identifier, version)
    if not extension_version['codelists']:
        abort(404)

    present_versions, historical_versions = get_present_and_historical_versions(extension)
    tables = get_codelist_tables(extension_version, lang)

    return render_template('extension_codelists.html', lang=lang, identifier=identifier, version=version,
                           extension=extension, extension_version=extension_version, present_versions=present_versions,
                           historical_versions=historical_versions, default_master=default_master, tables=tables)


@app.route('/<lang>/extensions/<identifier>/<version>/extension.json')
def extension_metadata_file(lang, identifier, version):
    extension, extension_version, _ = get_extension_and_version(identifier, version)

    return extension_version['metadata']


@app.route('/<lang>/extensions/<identifier>/<version>/README.md')
def extension_documentation_file(lang, identifier, version):
    extension, extension_version, _ = get_extension_and_version(identifier, version)
    if not extension_version['readme'][lang]:
        abort(404)

    return extension_version['readme'][lang], {'Content-Type': 'text/markdown; charset=utf-8'}


@app.route('/<lang>/extensions/<identifier>/<version>/<filename>')
def extension_schema_file(lang, identifier, version, filename):
    extension, extension_version, _ = get_extension_and_version(identifier, version)
    if not extension_version['schemas'][filename] or not extension_version['schemas'][filename][lang]:
        abort(404)

    return extension_version['schemas'][filename][lang]


@app.route('/<lang>/extensions/<identifier>/<version>/codelists/<filename>')
def extension_codelist_file(lang, identifier, version, filename):
    extension, extension_version, _ = get_extension_and_version(identifier, version)
    if not extension_version['codelists'][filename] or not extension_version['codelists'][filename][lang]:
        abort(404)

    codelist = extension_version['codelists'][filename][lang]

    io = StringIO()
    writer = csv.DictWriter(io, fieldnames=codelist['fieldnames'], lineterminator='\n', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(codelist['rows'])

    return io.getvalue(), {'Content-Type': 'text/csv; charset=utf-8'}
