=================
Aldryn Bootstrap3
=================


|pypi| |build| |coverage|

**Aldryn Bootstrap 3** is a plugin bundle for django CMS providing several
components from the popular `Bootstrap 3 <http://getbootstrap.com/>`_ framework.

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
`Transifex <https://www.transifex.com/projects/p/aldryn-bootstrap3/>`_.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/aldryn/aldryn-bootstrap3/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.6 or higher
* Django Filer 1.2.4 or higher
* Django Text CKEditor 3.1.0 or higher

Make sure `django Filer <http://django-filer.readthedocs.io/en/latest/installation.html>`_
and `django CMS Text CKEditor <https://github.com/divio/djangocms-text-ckeditor>`_
are installed and configured appropriately.


Installation
------------

For a manual install:

* run ``pip install aldryn-bootstrap3``
* add ``aldryn_bootstrap3`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate aldryn_bootstrap3``


Configuration
-------------

Aldryn Bootstrap 3 **replaces** the following django CMS plugins:

* **django CMS Link**: `Link and Button <http://getbootstrap.com/css/#buttons>`_
* **django CMS Picture**: `Image <http://getbootstrap.com/css/#images>`_
* **django CMS File**: `File <https://github.com/aldryn/aldryn-bootstrap3/wiki/14-file>`_

It provides the following **standard** Bootstrap 3 components:

* `Accordion <http://getbootstrap.com/javascript/#collapse-example-accordion>`_
* `Alert <http://getbootstrap.com/components/#alerts>`_
* `Blockquote <http://getbootstrap.com/css/#type-blockquotes>`_
* `Carousel <http://getbootstrap.com/javascript/#carousel>`_
* `Code <http://getbootstrap.com/css/#code>`_
* `Grid (Row and Column) <http://getbootstrap.com/css/#grid/>`_
* `Glyphicons <http://getbootstrap.com/components/#glyphicons>`_
* `Jumbotron <http://getbootstrap.com/components/#jumbotron>`_
* `Label <http://getbootstrap.com/components/#labels>`_
* `List Group <http://getbootstrap.com/components/#list-group>`_
* `Panel (Heading, Body and Footer) <http://getbootstrap.com/components/#panels>`_
* `Responsive <http://getbootstrap.com/css/#responsive-utilities>`_
* `Tabs <http://getbootstrap.com/javascript/#tabs>`_
* `Well <http://getbootstrap.com/components/#wells>`_

It also provides the following **3rd party** components:

* `Font Awesome <http://fontawesome.io>`_
* `Spacer <https://github.com/aldryn/aldryn-bootstrap3/wiki/13-spacer>`_

These components need to be manually configured in order to work properly
inside your project. See `this gist <https://gist.github.com/FinalAngel/40ea3fd48c0b9094ec7ded5d0e5d7395>`_
for additional information on a recommended spacer configuration.


Settings
~~~~~~~~

This addon provides a ``standard`` template for Carousels. You can provide
additional style choices by adding a ``ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES``
setting::

    ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES = [
        ('feature', _('Featured Version')),
    ]

You'll need to create the `feature` folder inside ``templates/aldryn_bootstrap/plugins/carousel/``
otherwise you will get a *template does not exist* error. You can do this by
copying the ``standard`` folder inside that directory and renaming it to
``feature``.

In addition you can set or extend your own icon fonts using ``ALDRYN_BOOTSTRAP3_ICONSETS``::

    ALDRYN_BOOTSTRAP3_ICONSETS = [
        ('glyphicons', 'glyphicons', 'Glyphicons'),
        ('fontawesome', 'fa', 'Font Awesome'),
        ('icons', 'icon', 'Custom Icons'),
    ]

The default grid size is set to **24** when validating the column input,
you can override this by setting::

    ALDRYN_BOOTSTRAP3_GRID_SIZE = 12


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/aldryn-bootstrap3.svg
    :target: http://badge.fury.io/py/aldryn-bootstrap3
.. |build| image:: https://travis-ci.org/aldryn/aldryn-bootstrap3.svg?branch=master
    :target: https://travis-ci.org/aldryn/aldryn-bootstrap3
.. |coverage| image:: https://codecov.io/gh/aldryn/aldryn-bootstrap3/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/aldryn/aldryn-bootstrap3
