=========
Changelog
=========


1.3.0 (unreleased)
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
