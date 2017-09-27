======================
django CMS Bootstrap 4
======================

**This addon is still in development, please do not use in production!**


|pypi| |build| |coverage|

**django CMS Bootstrap 4** is a plugin bundle for django CMS providing several
components from the popular `Bootstrap 4 <http://getbootstrap.com/>`_ framework.

This addon is compatible with `Divio Cloud <http://divio.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/aldryn-bootstrap3/>`_
for easy installation.

.. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

One of the easiest contributions you can make is helping to translate this addon on
`Transifex <https://www.transifex.com/projects/p/djangocms-bootstrap4/>`_.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-bootstrap4/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.8 or higher
* Django Filer 1.2.4 or higher
* Django Text CKEditor 3.1.0 or higher

Make sure `django Filer <http://django-filer.readthedocs.io/en/latest/installation.html>`_
and `django CMS Text CKEditor <https://github.com/divio/djangocms-text-ckeditor>`_
are installed and configured appropriately.


Installation
------------

For a manual install:

* run ``pip install djangocms-bootstrap4``
* add ``djangocms_bootstrap4`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_bootstrap4``


Configuration
-------------

django CMS Bootstrap 4 **utilises** the following django CMS plugins:

* **django CMS Link**: `Link and Button <http://getbootstrap.com/css/#buttons>`_
* **django CMS Picture**: `Image <http://getbootstrap.com/css/#images>`_
* **django CMS File**: `File <https://github.com/aldryn/aldryn-bootstrap3/wiki/14-file>`_

It provides the following **standard** Bootstrap 4 components:

* `Grid (Container, Row and Column) <https://getbootstrap.com/docs/4.0/layout/grid/>`_


Settings
~~~~~~~~

TBA


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/djangocms-bootstrap4.svg
    :target: http://badge.fury.io/py/djangocms-bootstrap4
.. |build| image:: https://travis-ci.org/divio/djangocms-bootstrap4.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-bootstrap4
.. |coverage| image:: https://codecov.io/gh/divio/djangocms-bootstrap4/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-bootstrap4
