import pytest
import responses

from swagger_stub_api.mock.utils import (
    load_file,
    parse_body,
    load_dict_from_path)


@pytest.fixture
def valid_path():
    return "./tests/fixtures/swagger.yaml"


@pytest.fixture
def valid_url():
    return "http://url.com/swagger.yaml"


def test_load_file_valid_path(valid_path):
    response = load_file(valid_path)
    assert type(response) == str


@responses.activate
def test_load_file_valid_url(valid_url, mocker):
    responses.add(responses.GET, valid_url, json={}, status=200)
    response = load_file(valid_url)
    assert type(response) == str


@pytest.mark.parametrize("body", [
    "{\"a\": 1}",
    """
  a: 1
"""])
def test_parse_body(body):
    response = parse_body(body)
    assert type(response) == dict


def test_load_dict_from_path(mocker, valid_path):
    mock_load_file = mocker.patch("swagger_stub_api.mock.utils.load_file",
                                  return_value="{}")

    mock_parse_body = mocker.patch("swagger_stub_api.mock.utils.parse_body",
                                   return_value={})

    assert load_dict_from_path(valid_path) == {}
    mock_load_file.assert_called_with(valid_path)
    mock_parse_body.assert_called_with(mock_load_file.return_value)
