# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import (
    TagTypeField,
    AttributesField,
)

from .constants import NAV_ALIGNMENT, NAV_STYLES


@python_2_unicode_compatible
class Bootstrap4Navs(CMSPlugin):
    """
    Components > "Navs" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    nav_style = models.CharField(
        verbose_name=_('Style'),
        choices=NAV_STYLES,
        blank=True,
        max_length=255,
    )
    nav_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=NAV_ALIGNMENT,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        if self.nav_style:
            text = '({}) '.format(self.nav_style)
        if self.nav_alignment:
            text += '{}'.format(self.nav_alignment)
        return text


@python_2_unicode_compatible
class Bootstrap4NavItem(CMSPlugin):
    """
    Components > "Nav Item" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return ''


@python_2_unicode_compatible
class Bootstrap4NavTabContent(CMSPlugin):
    """
    Components > "Nav Tab Content" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        return text


@python_2_unicode_compatible
class Bootstrap4NavTabPane(CMSPlugin):
    """
    Components > "Nav Tab Pane" Plugin
    https://getbootstrap.com/docs/4.0/components/navs/
    """
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        return text
