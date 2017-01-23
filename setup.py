#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from aldryn_bootstrap3 import __version__


REQUIREMENTS = [
    'django-appconf>=1.0.0',
    'django-cms>=3.3.0',
    'django-durationfield>=0.5.1',
    'django-filer>=0.9.11',
    'djangocms-text-ckeditor>=3.1.0',
    'djangocms-attributes-field>=0.1.1',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='aldryn-bootstrap3',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-bootstrap3',
    license='BSD',
    description=('Adds Bootstrap 3 components as plugins.'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
