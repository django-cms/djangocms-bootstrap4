# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField
from djangocms_bootstrap4.constants import DEVICE_CHOICES

from .constants import (
    SPACER_PROPERTY_CHOICES,
    SPACER_SIDE_CHOICES,
    SPACER_SIZE_CHOICES,
)


@python_2_unicode_compatible
class Bootstrap4Spacing(CMSPlugin):
    """
    Utilities > "Spacing" Plugin
    https://getbootstrap.com/docs/4.0/utilities/spacing/
    """
    space_property = models.CharField(
        verbose_name=_('Property'),
        choices=SPACER_PROPERTY_CHOICES,
        default=SPACER_PROPERTY_CHOICES[0][0],
        max_length=255,
    )
    space_sides = models.CharField(
        verbose_name=_('Sides'),
        choices=SPACER_SIDE_CHOICES,
        default=SPACER_SIDE_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    space_size = models.CharField(
        verbose_name=_('Size'),
        choices=SPACER_SIZE_CHOICES,
        default=SPACER_SIZE_CHOICES[0][0],
        max_length=255,
    )
    space_device = models.CharField(
        verbose_name=_('Device'),
        choices=DEVICE_CHOICES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_base_css_class(self):
        # Source: https://getbootstrap.com/docs/4.0/utilities/spacing/#notation
        # [...] format {property}{sides}-{size} for xs and {property}{sides}-{breakpoint}-{size} for sm, md, lg, and xl.
        if not self.space_device or self.space_device == 'xs':
            template = '{property}{sides}-{size}'
        else:
            template = '{property}{sides}-{breakpoint}-{size}'

        return template.format(
            property=self.space_property, sides=self.space_sides, breakpoint=self.space_device, size=self.space_size
        )

    def get_short_description(self):
        return '(.{})'.format(self.get_base_css_class())
