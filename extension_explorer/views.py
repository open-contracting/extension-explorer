from flask import Flask, abort
from flask import render_template
from flask_env import MetaFlaskEnv
import commonmark

from .extension_data import get_core_extensions, get_community_extensions, get_extension
from .util import create_toc, create_extension_tables, replace_directives, highlight_json


class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX = 'FLASK_'


app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def home():
    return lang_home('en')


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


@app.route('/<lang>/extension/<slug>/<version>/')
def extension(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)

        readme = extension_version.get("readme", {}).get(lang, {}).get("content", "")
        # WE SHOULD THINK HOW SAFE THIS IS
        readme_html = commonmark.commonmark(readme)
        readme_html, headings = create_toc(readme_html)

        extension_tables = create_extension_tables(extension_version, lang)
        readme_html = replace_directives(readme_html, extension_tables, lang, slug, version)

        readme_html, highlight_css = highlight_json(readme_html)

    except KeyError:
        abort(404)
    return render_template('extension_docs.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version,
                           readme_html=readme_html, headings=headings, highlight_css=highlight_css)


@app.route('/<lang>/extension/<slug>/<version>/info')
def extension_info(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
    except KeyError:
        abort(404)
    return render_template('extension_info.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version)


@app.route('/<lang>/extension/<slug>/<version>/reference')
def extension_reference(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
        extension_tables = create_extension_tables(extension_version, lang)
    except KeyError:
        abort(404)
    return render_template('schema_reference.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version,
                           extension_tables=extension_tables)


@app.route('/<lang>/extension/<slug>/<version>/codelists')
def extension_codelists(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
    except KeyError:
        abort(404)
    return render_template('extension_codelists.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version)
