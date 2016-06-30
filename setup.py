# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_bootstrap3 import __version__

REQUIREMENTS = [
    'django-appconf>=1.0.0',
    'django-cms>=3.0.10',
    'django-durationfield>=0.5.1',
    'django-filer>=0.9.11',
    'djangocms-attributes-field>=0.1.0',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='aldryn-bootstrap3',
    version=__version__,
    description='cms plugins and helpers for bootstrap3 based sites',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/aldryn/aldryn-bootstrap3',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    test_suite="test_settings.run",
)
