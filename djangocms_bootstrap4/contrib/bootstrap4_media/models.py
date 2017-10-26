# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField


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
