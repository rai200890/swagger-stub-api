import os
import os.path
from setuptools import setup, find_packages

rootdir = os.path.abspath(os.path.dirname(__file__))

install_requires = [
    "Flask>=0.11.1",
    "python-decouple>=3.1",
    "swagger-parser>=1.0.0",
    "Flask-Cors>=3.0.3",
    "click>=6.7"]

setup(name='swagger-stub-api',
      version='0.0.1',
      description='Swagger Stub API',
      url='https://github.com/rai200890/swagger-stub-api',
      author='Raissa Ferreira',
      author_email='rai2000890@gmail.com',
      classifiers=[
          'Natural Language :: English',
          'Programming Language :: Python :: 3'],
      keywords='swagger mock api',
      install_requires=install_requires,
      package_dir={"swagger_stub_api": "swagger_stub_api"},
      packages=["swagger_stub_api"],
      entry_points={
          "console_scripts": ["swagger-stub-api = swagger_stub_api.run:main"]})
