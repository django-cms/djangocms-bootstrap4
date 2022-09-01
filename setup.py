#!/usr/bin/env python
from setuptools import find_packages, setup

from djangocms_bootstrap4 import __version__


REQUIREMENTS = [
    'django-cms>=3.7',
    'django-filer>=1.7',
    'djangocms-attributes-field>=1',
    'djangocms-text-ckeditor>=3.1.0',
    'djangocms-icon>=1.4.0',
    'djangocms-link>=2.5.0',
    'djangocms-picture>=2.3.0',
]


EXTRA_REQUIREMENTS = {
    "static-ace": [
        "djangocms-static-ace",
    ]
}


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Framework :: Django',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.2',
    'Framework :: Django CMS',
    'Framework :: Django CMS :: 3.7',
    'Framework :: Django CMS :: 3.8',
    'Framework :: Django CMS :: 3.9',
    'Framework :: Django CMS :: 3.10',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries',
]


setup(
    name='djangocms-bootstrap4',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.ch',
    maintainer='Django CMS Association and contributors',
    maintainer_email='info@django-cms.org',
    url='https://github.com/django-cms/djangocms-bootstrap4',
    license='BSD-3-Clause',
    description='Adds Bootstrap 4 components as plugins.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude='tests'),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    extras_require=EXTRA_REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='tests.settings.run',
)
