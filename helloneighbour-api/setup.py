# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="COVID-19 Global Church Hack &#39;Hello Neighbour&#39;",
    author_email="",
    url="",
    keywords=["Swagger", "COVID-19 Global Church Hack &#39;Hello Neighbour&#39;"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    This is the API for COVID-19 Global Church Hack &#39;Hello Neighbour&#39; project
    """,
    zip_safe=False
)

