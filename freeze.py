from flask_frozen import Freezer

from extension_explorer.util import get_extensions
from extension_explorer.views import LANGS, app

freezer = Freezer(app)


@freezer.register_generator
def extension():
    for lang in LANGS:
        for identifier in get_extensions():
            yield {'lang': lang, 'identifier': identifier}


@freezer.register_generator
def extensions_json():
    yield {}


if __name__ == '__main__':
    freezer.freeze()
