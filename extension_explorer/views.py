from flask import Flask, abort
from flask import render_template
from flask_env import MetaFlaskEnv

from .extension_data import get_core_extensions, get_community_extensions, get_extension


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
    except KeyError:
        abort(404)
    return render_template('extension_docs.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version)


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
    except KeyError:
        abort(404)
    return render_template('schema_reference.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version)


@app.route('/<lang>/extension/<slug>/<version>/codelists')
def extension_codelists(lang, slug, version):
    try:
        extension, extension_version = get_extension(slug, version)
    except KeyError:
        abort(404)
    return render_template('extension_codelists.html', lang=lang, slug=slug, version=version,
                           extension=extension, extension_version=extension_version)
