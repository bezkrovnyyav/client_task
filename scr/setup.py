"""
Setup script for the scr package.

This script uses setuptools to define the package metadata, dependencies, and other configuration.

Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    packages (List[str]): A list of all Python packages to include.
    install_requires (List[str]): A list of dependencies required for the package.
    author(str): Name of the author.
    author_email(str): Emailof the author_email.
    url(str): URL of the repository with the app.

Example:
    To install the package along with its dependencies, use the following command:
        $ pip install .
"""

from setuptools import find_packages, setup

setup(
    name='client_service',
    version='0.1',
    packages=find_packages(),
    author='Andrii',
    author_email='bezkrovnyyav@email.com',
    description='App  get data from the site jsonplaceholder',
    url='https://github.com/bezkrovnyyav/client_task/tree/main',
    install_requires=[
        'requests',
    ],
)
