#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import find_packages, setup
import djangoRest2Typescript

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='djangoRest2Typescript',
    version=djangoRest2Typescript.__version__,
    #packages=find_packages(),
    packages=['djangoRest2Typescript', 'djangoRest2Typescript.migrations'],
    include_package_data=True,
    install_requires=[
        'django', 
    ],
    license=djangoRest2Typescript.__license__,  # example license
    description='From django serializers to typescript',
    long_description=README,
    url=djangoRest2Typescript.__url__,
    author=djangoRest2Typescript.__author__,
    author_email=djangoRest2Typescript.__author_email__,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',  # keep updated "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ' + djangoRest2Typescript.__license__,  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
