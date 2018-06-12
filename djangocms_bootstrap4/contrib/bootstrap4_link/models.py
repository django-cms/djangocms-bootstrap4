# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from djangocms_link.models import AbstractLink
from djangocms_icon.fields import Icon
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES

from .constants import LINK_CHOICES, LINK_SIZE_CHOICES


# 'link' type is added manually as it is only required for this plugin
COLOR_STYLE_CHOICES = (
    ('link', _('Link')),
) + COLOR_STYLE_CHOICES


@python_2_unicode_compatible
class Bootstrap4Link(AbstractLink):
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
        choices=COLOR_STYLE_CHOICES,
        blank=True,
        max_length=255,
    )
    link_size = models.CharField(
        verbose_name=_('Size'),
        choices=LINK_SIZE_CHOICES,
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
    icon_left = Icon(
        verbose_name=_('Icon left'),
    )
    icon_right = Icon(
        verbose_name=_('Icon right'),
    )

    def __str__(self):
        return str(self.pk)
