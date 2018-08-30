from flask_frozen import Freezer
from extension_explorer import views


freezer = Freezer(views.app)

if __name__ == '__main__':
    freezer.freeze()
