# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='visca',
    version=__import__("visca").__version__,
    packages=find_packages(),
    include_package_data=False,
    install_requires=[],
)
