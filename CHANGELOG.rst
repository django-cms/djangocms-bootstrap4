=========
Changelog
=========

3.0.2 2024-07-24
================

* fix: container replace gettext_lazy with gettext by @florianRepenn in https://github.com/django-cms/djangocms-bootstrap4/pull/164

**New Contributors**

* @florianRepenn made their first contribution in https://github.com/django-cms/djangocms-bootstrap4/pull/164



3.0.0 2022-09-01
================

* Added support for djangocms-static-ace to serve the ace code editor locally
* Added support for Django 3.2
* Dropped support for Python 3.7
* Dropped support for Django 3.0 and 3.1

2.0.0 (2020-09-02)
==================

* Added support for Django 3.1
* Dropped support for Python 2.7 and Python 3.4
* Dropped support for Django < 2.2
* Added support for sorl thumbnail
* Fixed CORS issues with external SVGs
* Fixed link preview not showing the correct icon
* Added documentation information about ``TEXT_SAVE_IMAGE_FUNCTION``


1.6.0 (2020-04-21)
==================

* Added support for Django 3.0
* Added support for Python 3.8
* Pinned ``django-filer`` to 1.5.0
* Added further tests to raise coverage
* Fixed smaller issues found during testing
* Dropped support for django-filer <= 1.4


1.5.0 (2019-07-09)
==================

* This update requires djangocms-link>=2.5.0
* This update requires djangocms-picture>=2.3.0
* Added new migrations for bootstrap link and picture plugins
* Fixes offset class not being rendered when set to 0
* Fixes order class not being rendered when set to 0


1.4.0 (2019-05-23)
==================

* This update requires djangocms-icon >= 1.4.0
* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Added isort and adapted imports
* Adapted code base to align with other supported addons
* Added option to add custom classes to carousel (#82)
* Fixes an issue where ``DJANGOCMS_BOOTSTRAP4_CAROUSEL_DEFAULT_SIZE`` is not honoured
* Fixes an issue on Divio Cloud where the addon is not installing djangocms-icon


1.3.1 (2018-12-20)
==================

* Fixed a regression where link became required in the carousel


1.3.0 (2018-12-13)
==================

* Added Django 2.x support
* Fixed test matrix
* Fixed an issues with links showing up twice in carousel (#69)
* Exclude ``tests`` folder from release build


1.2.0 (2018-11-15)
==================

* Removed support for Django 1.8, 1.9, 1.10
* Fixed a regression with spacing utilities rendering incorrectly
* Fixed a regression where migrations are failing


1.1.4 (2018-11-05)
==================

* Fixed a regression with collapse plugins


1.1.3 (2018-10-19)
==================

* Adapt Bootstrap4Picture to reflect djangocms_picture.AbstractPicture changes regarding Responsive Images (#65)


1.1.2 (2018-10-05)
==================

* Fix README migration command
* Fix Plural-Forms of i18n for english language
* Add <code> element inside <pre> in code block
* Fix spacing class for XS devices


1.1.1 (2018-07-17)
==================

* Fixed a bug where offset values wouldn't be rendered in bootstrap grid
* Fixed a bug where offset and order fields wouldn't allow for zeroes


1.1.0 (2018-07-11)
==================

* Added djangocms-icon to installation instructions
* Adapted test matrix
* Fixed linting
* Fixed carousel slide not starting at 0
* Fixed errors with some of the alignment fields
* Carousel aspect ratios modifiable from settings
* Fixed extra small breakpoint classes
* Removed column_size field, use xs_col instead
* Fixed column ui not fitting the CMS modal
* Color styles modifiable from settings


1.0.0 (2018-03-12)
==================

* Added further information to the README.rst
* General cleanup for release
* Added transifex translations


0.1.0 (unreleased)
==================

* This release is only available on Divio Cloud
* Added Media Plugin
* Added Tabs Plugin
* Added Icons Plugin
* Added Figure Plugin
* Added Code and Blockquote Plugin
* Added Icon support to Button / Link Plugin
* Various UI changes and fixes


0.0.1 (unreleased)
==================

* All 0.x.x releases will only be available as **alpha** on Divio Cloud
* Forked from https://github.com/aldryn/aldryn-bootstrap3
* Initial release
