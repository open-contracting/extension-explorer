import os

from flask import Flask, redirect, url_for
from flask import render_template
from flask_env import MetaFlaskEnv


class Configuration(metaclass=MetaFlaskEnv):
    ENV_PREFIX = 'FLASK_'

app = Flask(__name__)
app.config.from_object(Configuration)

@app.route('/')
def home():
    return lang_home('en')

@app.route('/<lang>/')
def lang_home(lang):
    return render_template('home.html')

@app.route('/<lang>/core/<version>/<extension>/')
def core(lang, version, extension):
    return render_template('home.html')

@app.route('/<lang>/community/<extension>/<version>')
def community(lang, extension, version):
    return render_template('home.html')
