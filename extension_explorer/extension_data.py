import os
import json
import collections


def get_data():
    if os.environ.get('EXTENSION_EXPLORER_DATA_FILE'):
        filename = os.environ.get('EXTENSION_EXPLORER_DATA_FILE')
    else:
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data.json')
    with open(filename) as extension_data_file:
        extension_data = json.load(extension_data_file, object_pairs_hook=collections.OrderedDict)

    return extension_data


def get_core_extensions():
    all_extension_data = get_data()
    core_extensions = []
    for extension_name in sorted(all_extension_data['extensions'].keys()):
        extension = all_extension_data['extensions'][extension_name]
        if not extension['core']:
            continue
        extension['slug'] = extension_name
        core_extensions.append(extension)
    return core_extensions


def get_community_extensions():
    all_extension_data = get_data()
    community_extensions = []
    for extension_name in sorted(all_extension_data['extensions'].keys()):
        extension = all_extension_data['extensions'][extension_name]
        if extension['core']:
            continue
        extension['slug'] = extension_name
        community_extensions.append(extension)
    return community_extensions


def get_extension(slug, version):
    all_extension_data = get_data()
    extension = all_extension_data['extensions'][slug]
    version = extension['versions'][version]

    return extension, version
