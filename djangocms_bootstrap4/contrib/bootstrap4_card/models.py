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
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES

from .constants import (
    CARD_TYPE_CHOICES,
    CARD_ALIGNMENT_CHOICES,
    CARD_INNER_TYPE_CHOICES,
)


# cards allow for a transparent color
CARD_COLOR_STYLE_CHOICES = COLOR_STYLE_CHOICES + (
    ('transparent', _('Transparent')),
)

CARD_TEXT_STYLES = COLOR_STYLE_CHOICES + (
    ('white', _('White')),
)


@python_2_unicode_compatible
class Bootstrap4Card(CMSPlugin):
    """
    Components > "Card" Plugin
    https://getbootstrap.com/docs/4.0/components/card/
    """
    card_type = models.CharField(
        verbose_name=_('Card type'),
        choices=CARD_TYPE_CHOICES,
        default=CARD_TYPE_CHOICES[0][0],
        max_length=255,
    )
    card_context = models.CharField(
        verbose_name=_('Background context'),
        choices=CARD_COLOR_STYLE_CHOICES,
        blank=True,
        max_length=255,
    )
    card_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=CARD_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
    )
    card_outline = models.BooleanField(
        verbose_name=_('Outline'),
        default=False,
        help_text=_('Uses the border context instead of the background.'),
    )
    card_text_color = models.CharField(
        verbose_name=_('Text context'),
        choices=CARD_TEXT_STYLES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = '({})'.format(self.card_type)
        if self.card_context and self.card_outline:
            text += ' .border-{}'.format(self.card_context)
        elif self.card_context:
            text += ' .bg-{}'.format(self.card_context)
        if self.card_alignment:
            text += ' .{}'.format(self.card_alignment)
        return text


@python_2_unicode_compatible
class Bootstrap4CardInner(CMSPlugin):
    """
    Components > "Card - Inner" Plugin (Header, Footer, Body)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    inner_type = models.CharField(
        verbose_name=_('Inner type'),
        choices=CARD_INNER_TYPE_CHOICES,
        default=CARD_INNER_TYPE_CHOICES[0][0],
        max_length=255,
        help_text=_('Define the structure of the plugin.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.inner_type)
