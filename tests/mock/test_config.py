import pytest
from swagger_parser import SwaggerParser

from swagger_stub_api.mock.config import MockResponseConfig


@pytest.fixture
def valid_path():
    return "./tests/fixtures/swagger.yaml"


def test_mock_response_config_swagger_parser(mocker, valid_path):
    mock_load_and_validate_swagger_file = mocker.patch("swagger_stub_api.mock.config.load_and_validate_swagger_file")
    SwaggerParserMock = mocker.patch("swagger_stub_api.mock.config.SwaggerParser")

    config = MockResponseConfig(valid_path)
    response = config.swagger_parser

    mock_load_and_validate_swagger_file.assert_called_with(valid_path)
    SwaggerParserMock.assert_called_with(swagger_dict=mock_load_and_validate_swagger_file.return_value)
    assert response == SwaggerParserMock.return_value
