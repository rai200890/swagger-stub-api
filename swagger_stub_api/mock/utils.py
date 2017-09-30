from flex.core import load, validate


def load_and_validate_swagger_file(swagger_path):
    schema = load(swagger_path)
    validate(schema)
    return schema
