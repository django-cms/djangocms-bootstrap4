======================
django CMS Bootstrap 4
======================

|pypi| |build| |coverage|

**django CMS Bootstrap 4** is a plugin bundle for django CMS providing several
components from the popular `Bootstrap 4 <http://getbootstrap.com/>`_ library.

.. note::

        This project is endorsed by the `django CMS Association <https://www.django-cms.org/en/about-us/>`_.
        That means that it is officially accepted by the dCA as being in line with our roadmap vision and development/plugin policy.
        Join us on `Slack <https://www.django-cms.org/slack/>`_.

.. image:: preview.gif


*******************************************
Contribute to this project and win rewards
*******************************************

Because this is a an open-source project, we welcome everyone to
`get involved in the project <https://www.django-cms.org/en/contribute/>`_ and
`receive a reward <https://www.django-cms.org/en/bounty-program/>`_ for their contribution.
Become part of a fantastic community and help us make django CMS the best CMS in the world.

We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

The project makes use of git pre-commit hooks to maintain code quality. Please follow the
installation steps to get `pre-commit <https://pre-commit.com/#installation>`_ setup in your development environment.

We're grateful to all contributors who have helped create and maintain this package.
Contributors are listed at the `contributors <https://github.com/django-cms/djangocms-bootstrap4/graphs/contributors>`_
section.


Documentation
=============

See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-bootstrap4/blob/master/setup.py>`_
file for additional dependencies:

|python| |django| |djangocms|

* Django Filer 1.7 or higher
* Django Text CKEditor 3.1 or higher

Make sure `django Filer <http://django-filer.readthedocs.io/en/latest/installation.html>`_
and `django CMS Text CKEditor <https://github.com/divio/djangocms-text-ckeditor>`_
are installed and configured appropriately.


Installation
------------

For a manual install:

* run ``pip install djangocms-bootstrap4``
* add the following entries to your ``INSTALLED_APPS``::

    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',

* run ``python manage.py migrate``

The Code plugin uses the ace code editor which is loaded from a CDN by default.
If you want the ace code editor to be served from static files, please use
``djangocms-bootstrap4[static-ace]`` instead of ``djangocms-bootstrap4`` in your
requirements or with pip. Make the static files fore the ace code editor available
to your project by adding ``djangocms_static_ace`` to your project's
``INSTALLED_APPS``.


Configuration
-------------

django CMS Bootstrap 4 **utilises** the following django CMS plugins:

* **django CMS Link**: `Link <https://github.com/divio/djangocms-link/>`_
* **django CMS Picture**: `Picture <https://github.com/divio/djangocms-picture/>`_
* **django CMS Icon**: `Icon <https://github.com/divio/djangocms-icon>`_

It provides the following **standard** Bootstrap 4 components:

* `Alerts <https://getbootstrap.com/docs/4.0/components/alerts/>`_
* `Badge <https://getbootstrap.com/docs/4.0/components/badge/>`_
* `Card <https://getbootstrap.com/docs/4.0/components/card/>`_
* `Carousel <https://getbootstrap.com/docs/4.0/components/carousel/>`_
* `Collapse <https://getbootstrap.com/docs/4.0/components/collapse/>`_
* `Content (Blockquote, Code, Figure) <https://getbootstrap.com/docs/4.0/content/>`_
* `Grid (Container, Row, Column) <https://getbootstrap.com/docs/4.0/layout/grid/>`_
* `Jumbotron <https://getbootstrap.com/docs/4.0/components/jumbotron/>`_
* `Link / Button <https://getbootstrap.com/docs/4.0/components/buttons/>`_
* `List group <https://getbootstrap.com/docs/4.0/components/list-group/>`_
* `Media <https://getbootstrap.com/docs/4.0/layout/media-object/>`_
* `Picture / Image <https://getbootstrap.com/docs/4.0/content/images/>`_
* `Tabs <https://getbootstrap.com/docs/4.0/components/navs/#tabs>`_
* `Utilities (Spacing) <https://getbootstrap.com/docs/4.0/utilities/>`_

django CMS Bootstrap 4 **does not** add the styles or javascript files to your
frontend, these need to be added at your discretion.


Settings
~~~~~~~~

There are various settings possible on django CMS Bootstrap 4, to restrict them
for now only the following can be changed::

    DJANGOCMS_BOOTSTRAP4_TAG_CHOICES = ['div', 'section', 'article', 'header', 'footer', 'aside']

    DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES = (
        ('default', _('Default')),
    )

    DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 12
    DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = (
        (_('Default'), (
            ('container', _('Container')),
            ('container-fluid', _('Fluid container')),
        )),
        (_('Custom'), (
            ('container-yours', _('Your container')),
        )),
    )
    DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
        ('col', _('Column')),
        ('w-100', _('Break')),
        ('', _('Empty'))
    )

    DJANGOCMS_BOOTSTRAP4_USE_ICONS = True

    DJANGOCMS_BOOTSTRAP4_TAB_TEMPLATES = (
        ('default', _('Default')),
    )

    DJANGOCMS_BOOTSTRAP4_SPACER_SIZES = (
        ('0', '* 0'),
        ('1', '* .25'),
        ('2', '* .5'),
        ('3', '* 1'),
        ('4', '* 1.5'),
        ('5', '* 3'),
    )

    DJANGOCMS_BOOTSTRAP4_CAROUSEL_ASPECT_RATIOS = (
        (16, 9),
    )

    DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES = (
        ('primary', _('Primary')),
        ('secondary', _('Secondary')),
        ('success', _('Success')),
        ('danger', _('Danger')),
        ('warning', _('Warning')),
        ('info', _('Info')),
        ('light', _('Light')),
        ('dark', _('Dark')),
        ('custom', _('Custom')),
    )

Please be aware that this package does not support djangocms-text-ckeditor's
`Drag & Drop Images <https://github.com/divio/djangocms-text-ckeditor/#drag--drop-images>`_
so be sure to set ``TEXT_SAVE_IMAGE_FUNCTION = None``.


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements/djNN_cmsNN.txt # where NN is an available appropriate version
    python setup.py test

To run the frontend make sure to use **node 10.x**.


.. |pypi| image:: https://badge.fury.io/py/djangocms-bootstrap4.svg
    :target: http://badge.fury.io/py/djangocms-bootstrap4
.. |build| image:: https://travis-ci.org/divio/djangocms-bootstrap4.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-bootstrap4
.. |coverage| image:: https://codecov.io/gh/divio/djangocms-bootstrap4/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-bootstrap4

.. |python| image:: https://img.shields.io/badge/python-3.5+-blue.svg
    :target: https://pypi.org/project/djangocms-bootstrap4/
.. |django| image:: https://img.shields.io/badge/django-2.2,%203.0,%203.1-blue.svg
    :target: https://www.djangoproject.com/
.. |djangocms| image:: https://img.shields.io/badge/django%20CMS-3.7%2B-blue.svg
    :target: https://www.django-cms.org/
