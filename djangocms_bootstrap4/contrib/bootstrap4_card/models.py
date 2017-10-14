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
from djangocms_bootstrap4.constants import COLOR_STYLES

from .constants import (
    CARD_TYPES,
    CARD_ALIGNMENT,
    CARD_INNER_TYPE,
    CARD_CONTENT_TYPE,
    CARD_TAG_CHOICES,
    CARD_IMAGE_TYPE,
)


# cards allow for a transparent color
CARD_COLOR_STYLES = COLOR_STYLES + (
    ('transparent', _('Transparent')),
)

CARD_TEXT_STYLES = COLOR_STYLES + (
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
        choices=CARD_TYPES,
        default=CARD_TYPES[0][0],
        max_length=255,
    )
    card_context = models.CharField(
        verbose_name=_('Context'),
        choices=CARD_COLOR_STYLES,
        blank=True,
        max_length=255,
    )
    card_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=CARD_ALIGNMENT,
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
        choices=CARD_INNER_TYPE,
        default=CARD_INNER_TYPE[0][0],
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.inner_type)


@python_2_unicode_compatible
class Bootstrap4CardContent(CMSPlugin):
    """
    Components > "Card - Content" Plugin (Title, Subtitle, Text, Link)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    content_type = models.CharField(
        verbose_name=_('Content type'),
        choices=CARD_CONTENT_TYPE,
        default=CARD_CONTENT_TYPE[0][0],
        max_length=255,
    )
    card_content = models.CharField(
        verbose_name=_('Content'),
        blank=True,
        max_length=255,
        help_text=_('Use this to display a simple text, alternatively you can use nested plugins.'),
    )
    tag_type = TagTypeField(
        choices=CARD_TAG_CHOICES,
        default=CARD_TAG_CHOICES[0][0],
    )
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.content_type)


@python_2_unicode_compatible
class Bootstrap4CardImage(CMSPlugin):
    """
    Components > "Card - Image" Plugin (Top, Bottom, Overlay)
    https://getbootstrap.com/docs/4.0/components/card/
    """
    content_type = models.CharField(
        verbose_name=_('Image type'),
        choices=CARD_IMAGE_TYPE,
        default=CARD_IMAGE_TYPE[0][0],
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.content_type)
