import commonmark
from flask import Flask, abort, redirect, request, url_for
from flask import render_template
from flask_babel import Babel
from flask_env import MetaFlaskEnv

from .extension_data import get_core_extensions, get_community_extensions, get_extension
from .util import get_schema_tables, identify_headings, highlight_json
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


@app.route('/')
def home():
    return redirect(url_for('lang_home', lang='en'))


@app.route('/<lang>/')
def lang_home(lang):
    return render_template('home.html', lang=lang)


@app.route('/<lang>/core/')
def core(lang):
    data = get_core_extensions()
    return render_template('core.html', lang=lang, data=data)


@app.route('/<lang>/community/')
def community(lang):
    data = get_community_extensions()
    return render_template('community.html', lang=lang, data=data)


@app.route('/<lang>/extensions/<slug>/<version>/')
def extension(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)

        tables = get_schema_tables(extension_version, lang)

        # Note: `readme` may contain unsafe HTML and JavaScript.
        schema_url = url_for('extension_reference', lang=lang, slug=slug, version=version)
        codelist_url = url_for('extension_codelists', lang=lang, slug=slug, version=version)
        readme = extension_version.get('readme', {}).get(lang, {}).get('content', '')
        readme_html = commonmark.commonmark(readme)
        readme_html, headings = identify_headings(readme_html)
        readme_html = replace_directives(readme_html, schema_url, codelist_url, tables)
        readme_html, highlight_css = highlight_json(readme_html)
    except KeyError:
        abort(404)
    return render_template('extension_docs.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version, readme_html=readme_html, headings=headings,
                           highlight_css=highlight_css)


@app.route('/<lang>/extensions/<slug>/<version>/info/')
def extension_info(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
    except KeyError:
        abort(404)
    return render_template('extension_info.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version)


@app.route('/<lang>/extensions/<slug>/<version>/reference/')
def extension_reference(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)

        tables = get_schema_tables(extension_version, lang)
    except KeyError:
        abort(404)
    return render_template('schema_reference.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version, extension_tables=tables)


@app.route('/<lang>/extensions/<slug>/<version>/codelists/')
def extension_codelists(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
    except KeyError:
        abort(404)
    return render_template('extension_codelists.html', lang=lang, slug=slug, version=version, extension=extension,
                           extension_version=extension_version)
