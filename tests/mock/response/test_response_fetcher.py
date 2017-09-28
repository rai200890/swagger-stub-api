import pytest

from swagger_stub_api.mock.response import ResponseFetcher


@pytest.fixture
def config_mock(mocker):
    return mocker.MagicMock()


@pytest.fixture
def request_mock(mocker):
    return mocker.MagicMock(method="get", data=b"{}")


@pytest.fixture
def RequestParserMock(mocker):
    return mocker.patch("swagger_stub_api.mock.response.RequestParser")


def test_swagger_parser(config_mock, request_mock):
    response_fetcher = ResponseFetcher(config_mock, request_mock, path="/v2/pets/1")

    assert response_fetcher.swagger_parser == config_mock.swagger_parser


def test_request_parser(RequestParserMock, config_mock, request_mock):
    response_fetcher = ResponseFetcher(config_mock, request_mock, path="/v2/pets/1")

    assert response_fetcher.request_parser == RequestParserMock.return_value
    RequestParserMock.assert_called_with(request_mock, response_fetcher.path)


def test_response(config_mock, request_mock):
    response_fetcher = ResponseFetcher(config_mock, request_mock, path="v2/pets/1")

    assert response_fetcher.response == config_mock.swagger_parser.get_request_data.return_value
    config_mock.swagger_parser.get_request_data.assert_called_with('/v2/pets/1', 'get', body='{}')


def test_fetch(config_mock, request_mock, mocker):
    config_mock.swagger_parser.get_request_data.return_value = {"200": {}}
    response_fetcher = ResponseFetcher(config_mock, request_mock, path="v2/pets/1")

    assert response_fetcher.fetch() == (200, {})
