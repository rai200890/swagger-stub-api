from swagger_parser import SwaggerParser

from .utils import load_and_validate_swagger_file


class MockResponseConfig(object):

    def __init__(self, swagger_path, validate_request=False):
        self.swagger_path = swagger_path
        self.validate_request = validate_request

    @property
    def swagger_parser(self):
        swagger_dict = load_and_validate_swagger_file(self.swagger_path)
        return SwaggerParser(swagger_dict=swagger_dict)
