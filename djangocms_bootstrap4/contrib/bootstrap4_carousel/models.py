# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags

from cms.models import CMSPlugin

from djangocms_link.models import AbstractLink
from djangocms_text_ckeditor.fields import HTMLField

from filer.fields.image import FilerImageField

from djangocms_bootstrap4.fields import TagTypeField, AttributesField

from .constants import (
    CAROUSEL_TEMPLATE_CHOICES,
    CAROUSEL_PAUSE_CHOICES,
    CAROUSEL_RIDE_CHOICES,
    CAROUSEL_ASPECT_RATIO_CHOICES,
)


@python_2_unicode_compatible
class Bootstrap4Carousel(CMSPlugin):
    """
    Components > "Carousel" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    template = models.CharField(
        verbose_name=_('Template'),
        choices=CAROUSEL_TEMPLATE_CHOICES,
        default=CAROUSEL_TEMPLATE_CHOICES[0][0],
        max_length=255,
        help_text=_('This is the template that will be used for the component.'),
    )
    carousel_interval = models.IntegerField(
        verbose_name=_('Interval'),
        default=5000,
        help_text=_('The amount of time to delay between automatically cycling '
                    'an item. If false, carousel will not automatically cycle.'),
    )
    carousel_controls = models.BooleanField(
        verbose_name=_('Controls'),
        default=True,
        help_text=_('Adding in the previous and next controls.'),
    )
    carousel_indicators = models.BooleanField(
        verbose_name=_('Indicators'),
        default=True,
        help_text=_('Adding in the indicators to the carousel.'),
    )
    carousel_keyboard = models.BooleanField(
        verbose_name=_('Keyboard'),
        default=True,
        help_text=_('Whether the carousel should react to keyboard events.'),
    )
    carousel_pause = models.CharField(
        verbose_name=_('Pause'),
        choices=CAROUSEL_PAUSE_CHOICES,
        default=CAROUSEL_PAUSE_CHOICES[0][0],
        max_length=255,
        help_text=_('If set to "hover", pauses the cycling of the carousel on '
                    '"mouseenter" and resumes the cycling of the carousel on '
                    '"mouseleave". If set to "false", hovering over the carousel '
                    'won\'t pause it.')
    )
    carousel_ride = models.CharField(
        verbose_name=_('Ride'),
        choices=CAROUSEL_RIDE_CHOICES,
        default=CAROUSEL_RIDE_CHOICES[0][0],
        max_length=255,
        help_text=_('Autoplays the carousel after the user manually cycles the '
                    'first item. If "carousel", autoplays the carousel on load.'),
    )
    carousel_wrap = models.BooleanField(
        verbose_name=_('Wrap'),
        default=True,
        help_text=_('Whether the carousel should cycle continuously or have '
                    'hard stops.'),
    )
    carousel_aspect_ratio = models.CharField(
        verbose_name=_('Aspect ratio'),
        choices=CAROUSEL_ASPECT_RATIO_CHOICES,
        blank=True,
        default='',
        max_length=255,
        help_text=_('Determines width and height of the image '
                    'according to the selected ratio.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField(
        excluded_keys=[
            'id', 'data-interval', 'data-keyboard',
            'data-pause', 'data-ride', 'data-wrap'
        ],
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = '({})'.format(self.template)
        text += ' {}: {}'.format(_('Interval'), self.carousel_interval)
        text += ', {}: {}'.format(_('Controls'), self.carousel_controls)
        text += ', {}: {}'.format(_('Indicators'), self.carousel_indicators)
        text += ', {}: {}'.format(_('Keyboard'), self.carousel_keyboard)
        text += ', {}: {}'.format(_('Pause'), self.carousel_pause)
        text += ', {}: {}'.format(_('Ride'), self.carousel_ride)
        text += '{}: {}'.format(_('Wrap'), self.carousel_wrap)
        return text


@python_2_unicode_compatible
class Bootstrap4CarouselSlide(AbstractLink):
    """
    Components > "Slide" Plugin
    https://getbootstrap.com/docs/4.0/components/carousel/
    """
    carousel_image = FilerImageField(
        verbose_name=_('Slide image'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    carousel_content = HTMLField(
        verbose_name=_('Content'),
        blank=True,
        default='',
        help_text=_('Content may also be added using child plugins.'),
    )
    tag_type = TagTypeField()

    def __str__(self):
        return str(self.pk)

    def clean(self):
        super(AbstractLink, self).clean()

    def get_link(self):
        return AbstractLink.get_link(self)

    def get_short_description(self):
        image_text = content_text = ''

        if self.carousel_image_id:
            if self.carousel_image.name:
                image_text = self.carousel_image.name
            elif self.carousel_image.original_filename \
                    and os.path.split(self.carousel_image.original_filename)[1]:
                image_text = os.path.split(self.carousel_image.original_filename)[1]
            else:
                image_text = 'Image'
        if self.carousel_content:
            text = strip_tags(self.carousel_content).strip()
            if len(text) > 100:
                content_text = '{}...'.format(text[:100])
            else:
                content_text = '{}'.format(text)

        if image_text and content_text:
            return '{} ({})'.format(image_text, content_text)
        else:
            return image_text or content_text
