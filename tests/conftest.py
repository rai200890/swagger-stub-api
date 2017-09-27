import pytest
from swagger_stub_api.app import app as _app


@pytest.fixture(scope="session")
def app(request):
    ctx = _app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app


@pytest.fixture
def test_client(app):
    return app.test_client()
