from setuptools import setup, find_packages

setup(
    name='ocdsextensionexplorer',
    version='0.0.0',
    packages=find_packages(),
    entry_points={
        'babel.extractors': [
            'collection = extension_explorer.extract:extract_collection',
        ],
    },
)