#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import setuptools

setuptools.setup(
    name="easy_allure",
    description="Library for allure testops",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="1.0.0",
    license="Apache-2.0",
    author="2GIS Test Labs",
    author_email="test-labs@2gis.ru",
    python_requires=">=3.7",
    packages=['easy_allure'],
    entry_points={
        'console_scripts': [
            'easy_allure = easy_allure.main:main'
        ]
    },
    package_data={'easy_allure': ['lib/*']},
    zip_safe=False,
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
