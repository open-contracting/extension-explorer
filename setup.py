from setuptools import find_packages, setup

setup(
    name='ocdsextensionexplorer',
    version='0.0.0',
    license='BSD',
    packages=find_packages(),
    entry_points={
        'babel.extractors': [
            'tag = extension_explorer.extract:extract_tag',
        ],
    },
)
