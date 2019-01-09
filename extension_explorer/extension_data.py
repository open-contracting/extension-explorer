import os
import json
from collections import OrderedDict


def get_data():
    if os.environ.get('EXTENSION_EXPLORER_DATA_FILE'):
        filename = os.environ.get('EXTENSION_EXPLORER_DATA_FILE')
    else:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
    with open(filename) as f:
        extension_data = json.load(f, object_pairs_hook=OrderedDict)

    return extension_data


def filter_extensions(extension_data, condition):
    all_extension_data = get_data()
    extensions = []
    for slug in sorted(all_extension_data):
        extension = all_extension_data[slug]
        if condition(extension):
            extension['slug'] = slug
            extensions.append(extension)
    return extensions


def get_core_extensions():
    return filter_extensions(get_data(), lambda extension: extension['core'])


def get_community_extensions():
    return filter_extensions(get_data(), lambda extension: not extension['core'])


def get_extension(slug, version):
    all_extension_data = get_data()
    extension = all_extension_data[slug]
    version = extension['versions'][version]

    return extension, version
