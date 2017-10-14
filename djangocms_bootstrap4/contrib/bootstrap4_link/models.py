# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_link.models import AbstractLink
from djangocms_bootstrap4.constants import COLOR_STYLES

from .constants import LINK_CHOICES, LINK_SIZES


# 'link' type is added manually as it is only required for this plugin
COLOR_STYLES = (
    ('link', _('Link')),
) + COLOR_STYLES


@python_2_unicode_compatible
class Bootstrap4Link(AbstractLink, CMSPlugin):
    """
    Components > "Button" Plugin
    https://getbootstrap.com/docs/4.0/components/buttons/
    """
    link_type = models.CharField(
        verbose_name=_('Type'),
        choices=LINK_CHOICES,
        default=LINK_CHOICES[0][0],
        max_length=255,
        help_text=_('Adds either the .btn-* or .text-* classes.'),
    )
    link_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLES,
        blank=True,
        max_length=255,
    )
    link_size = models.CharField(
        verbose_name=_('Size'),
        choices=LINK_SIZES,
        blank=True,
        max_length=255,
    )
    link_outline = models.BooleanField(
        verbose_name=_('Outline'),
        default=False,
        help_text=_('Applies the .btn-outline class to the elements.'),
    )
    link_block = models.BooleanField(
        verbose_name=_('Block'),
        default=False,
        help_text=_('Extends the button to the width of its container.'),
    )

    def __str__(self):
        return str(self.pk)
