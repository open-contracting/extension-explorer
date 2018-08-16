import os 
import json
import collections

cur_dir = os.path.dirname(os.path.realpath(__file__))

def get_data():
    with open(os.path.join(cur_dir, 'local_data.json')) as extension_data_file:
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
        extension['first_version'] = list(extension['versions'])[0]
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
        extension['first_version'] = list(extension['versions'])[0]
        community_extensions.append(extension)
    return community_extensions

def get_extension(slug, version):
    all_extension_data = get_data()
    extension = all_extension_data['extensions'][slug]
    version = extension['versions'][version]

    return extension, version



