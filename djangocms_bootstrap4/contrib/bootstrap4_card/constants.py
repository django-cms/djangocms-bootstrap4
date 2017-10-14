# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.utils.translation import ugettext_lazy as _


CARD_BLUEPRINTS = (
    ('', '-----'),
    ('card', _('Card')), # image, body (title, text, button)
    ('panel', _('Panel')), # header, body (title, text, button)
    ('teaser', _('Teaser')), # body (title, text, button)
    ('overlay', _('Overlay')), # img, overlay (title, text)
)

CARD_TYPES = (
    ('card', _('Card')),
    ('card-group', _('Card group')),
    ('card-deck', _('Card deck')),
    ('card-columns', _('Card columns')),
)

CARD_ALIGNMENT = (
    ('text-left', _('Left')),
    ('text-center', _('Center')),
    ('text-right', _('Right')),
)

CARD_INNER_TYPE = (
    ('card-header', _('Header')),
    ('card-body', _('Body')),
    ('card-footer', _('Footer')),
)

CARD_CONTENT_TYPE = (
    ('card-text', _('Text')),
    ('card-title', _('Title')),
    ('card-subtitle', _('Subtitle')),
    ('card-link', _('Link')),
)

CARD_TAG_CHOICES = (
    ('div', 'DIV'),
    ('h1', 'H1'),
    ('h2', 'H2'),
    ('h3', 'H3'),
    ('h4', 'H4'),
    ('h5', 'H5'),
    ('h6', 'H6'),
    ('p', 'P'),
    ('small', 'SMALL'),
)

CARD_IMAGE_TYPE = (
    ('card-img-top', _('Image top')),
    ('card-img-bottom', _('Image bottom')),
    ('card-img-overlay', _('Image overlay')),
)
