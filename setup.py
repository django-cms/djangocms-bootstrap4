# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_bootstrap3 import __version__

REQUIREMENTS = [

]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
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
    dependency_links=[
        'git+https://github.com/yakky/django-cms@future/integration#egg=django-cms-3.0.90a3',
        'git+https://github.com/aldryn/aldryn-apphooks-config#egg=aldryn-apphooks-config-0.1.0',
    ],
)
