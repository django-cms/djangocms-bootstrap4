# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from cms.models import CMSPlugin

from six import python_2_unicode_compatible

from djangocms_bootstrap4.fields import AttributesField, TagTypeField


@python_2_unicode_compatible
class Bootstrap4Media(CMSPlugin):
    """
    Layout > "Media" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return ''


@python_2_unicode_compatible
class Bootstrap4MediaBody(CMSPlugin):
    """
    Layout > "Media body" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return ''
