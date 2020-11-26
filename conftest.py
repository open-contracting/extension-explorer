import pytest

from extension_explorer.views import app as flask_app


@pytest.fixture()
def app():
    return flask_app
