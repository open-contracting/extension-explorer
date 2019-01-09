from flask_frozen import Freezer

from extension_explorer.views import app


freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
