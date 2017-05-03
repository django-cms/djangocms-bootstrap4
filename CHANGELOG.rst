=========
Changelog
=========


1.2.2 (unreleased)
==================

* Fixed a bug which prevented links from working when the page
  referenced is on a different site from the one that contains the plugin.
* Removed unused and deprecated django-durationfield from requirements


1.2.1 (2017-03-07)
==================

* Removed link restriction when no link is provided to the carousel
* Fixed an issue where selecting the "Use original image" option is not
  rendering the image


1.2.0 (2017-01-26)
==================

* Added Django 1.10 support
* Added <code> plugin
* Added <cite> plugin to <blockquote>
* Added responsive plugin to set device and print breakpoints
* Added tab and tab item plugins
* Added attributes fields to models missing it
* Added missing translation declarations to untranslated strings
* Added default CKEditor "styleSet" to load via djangocms-text-ckeditor in
  ``/static/aldryn_bootstrap3/js/ckeditor.js``
* Added transifex integration for translations
* Added test framework
* Changed root files such as ``README``, ``CHANGELOG``, ``setup.py`` and others
  to conform with other core addons such as django CMS Picture
* Changed labels and help texts of several plugins
* Changed all max_values to 255
* Changed code to reflect Bootstrap 3's documentation
* Fixed an issue with collapse styles from image plugin overriding bootstrap
  styles already on the page
* Fixed an issue with dropzone strings visible inside djangocms-text-ckeditor
  image preview under certain circumstances
* Fixed an issue where column offset, push and pull did not accept "0" as a value
* **Backwards incompatible** changes:
    * The Panel only allows header, body and footer now to be its direct
      decendands and the descendends require the "Panel" parent.
    * Drag & drop support has been removed from the rendered plugin markup
      until a cleaner version is ready
    * Simplified and removed constants such as ``LABEL_CONTEXT_CHOICES``,
      ``LABEL_CONTEXT_DEFAULT``, ,``TEXT_LINK_CONTEXT_CHOICES``,
      ``TXT_LINK_CONTEXT_DEFAULT``, ``PANEL_CONTEXT_CHOICES``,
      ``PANEL_CONTEXT_DEFAULT``, ``ACCORDION_ITEM_CONTEXT_CHOICES``,
      ``ACCORDION_ITEM_CONTEXT_DEFAULT``, ``LIST_GROUP_ITEM_CONTEXT_CHOICES``,
      ``LIST_GROUP_ITEM_CONTEXT_DEFAULT``


1.1.2 (2016-09-05)
==================

* Let attributes field be optional
* Fixed styling issues with attributes field
* Changed the "label" plugin template to include no whitespace inside or
  outside the span
* Pinned djangocms-attributes-field to v0.1.1+
* Disabled "text preview" for the Spacer plugin
* Changed JavaScript to allow custom iconsets
* Improved edit mode preview of image plugin
* Fixed a bug in Link/Button plugin preview not always respecting icon options
* Added missing migrations for djangoCMS 3.3.1 compatibility.
* Added class "js-ckeditor-use-selected-text" to the label field on the
  Bootstrap3LabelCMSPlugin and Bootstrap3ButtonCMSPlugin plugins
* Introduced support for djangoCMS 3.4.0


1.1.1 (2016-07-05)
==================

* Pinned djangocms-attributes-field v0.1.0
* Fixed issue with template


1.1.0 (2016-06-20)
==================

* Added support for arbitrary attributes on link tags
* Fixed a Python 3 incompatibility
* Allow zero values for column push, pull and offset in admin forms
* Added a "change" event trigger when changing bootstrap style for multiple
  plugins


1.0.10 (2016-04-27)
===================

* Removes spaces before and after link
* Fixes drag and drop image view in edit mode for xplorer
* Updates upload info box styles


1.0.9 (2016-03-16)
==================

* Removes unnecessary `cache = False` from plugins


1.0.8 (2016-02-22)
==================

* Add drag-n-drop for image plugin in content mode


1.0.7 (2016-01-13)
==================

* Remove imagePlugin reference
* Add drag and drop support for image plugin in content mode
  (if supported by Django Filer).
* Fix name display for file plugin
* Add original image checkbox


1.0.6 (2015-12-14)
==================

* Allow children in link plugin
* Make image in carousel slide plugin mandatory
* Make image in image plugin mandatory
* Replace `xrange` with `range`
* Remove preview for image


1.0.5 (2015-11-26)
==================

* Upload correct version


1.0.4 (2015-11-24)
==================

* Move extra width and height for image to advanced section
* Change how image label is retrieved (fixes nonexistent image issue)


1.0.3 (2015-11-19)
==================

* Fixed an issue with links not rendering target
* Fixed an issue with links rendering empty class attribute
* Enhance display of image name in structure board


1.0.2 (2015-11-17)
==================

* Adds static folder to include in MANIFEST.in


1.0.1 (2015-11-17)
==================

* Fixes preview display for all plugins and widgets
* Implement icons for text_enabled plugins
* Add width and height configuration to image plugin
* Code cleanup


1.0.0 (2015-11-03)
==================

* Initial release
