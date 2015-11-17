# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
from .conf import settings

CONTEXT_CHOICES = (
    ('primary', 'Primary',),
    ('success', 'Success',),
    ('info', 'Info',),
    ('warning', 'Warning',),
    ('danger', 'Danger',),
)
CONTEXT_DEFAULT = 'default'

BUTTON_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    ('link', 'Link',),
)
BUTTON_CONTEXT_DEFAULT = 'default'

TXT_LINK_CONTEXT_CHOICES = (
    ('', 'Default',),
) + CONTEXT_CHOICES + (
    ('muted ', 'Muted',),
)
TXT_LINK_CONTEXT_DEFAULT = ''

LABEL_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    # ('', 'Custom',),
)
LABEL_CONTEXT_DEFAULT = 'default'

PANEL_CONTEXT_CHOICES = (
    ('default', 'Default',),
) + CONTEXT_CHOICES + (
    # ('', 'Custom',),
)
PANEL_CONTEXT_DEFAULT = 'default'

ACCORDION_ITEM_CONTEXT_CHOICES = PANEL_CONTEXT_CHOICES
ACCORDION_ITEM_CONTEXT_DEFAULT = PANEL_CONTEXT_DEFAULT

LIST_GROUP_ITEM_CONTEXT_CHOICES = (
    ('', 'Default',),
) + CONTEXT_CHOICES
LIST_GROUP_ITEM_CONTEXT_DEFAULT = ''

SIZE_CHOICES = (
    ('lg', 'Large',),
    ('md', 'Medium',),
    ('sm', 'Small',),
    ('xs', 'Extra Small',),
)

SIZE_WIDGET_CHOICES = (
    # ('', 'Default'),
) + SIZE_CHOICES
SIZE_WIDGET_DEFAULT = 'md'

SIZES = tuple([size for size, name in SIZE_CHOICES])

SIZE_DEFAULT = 'md'


# WARNING: changing DEVICE_CHOICES identifier will cause model creation to change and
#          requires database migrations!
DEVICES = (
    {
        'identifier': 'xs',
        'name': _("mobile phones"),
        'width': 768,
        'width_gutter': 750,
        'icon': 'mobile-phone',
    },
    {
        'identifier': 'sm',
        'name': _("tablets"),
        'width': 768,
        'width_gutter': 750,
        'icon': 'tablet',
    },
    {
        'identifier': 'md',
        'name': _("laptops"),
        'width': 992,
        'width_gutter': 970,
        'icon': 'laptop',
    },
    {
        'identifier': 'lg',
        'name': _("large desktops"),
        'width': 1200,
        'width_gutter': 1170,
        'icon': 'desktop',
    },
)
for device in DEVICES:
    identifier = device['identifier']
    device['long_description'] = "{name} (<{width}px)".format(**device)
    device['size_name'] = dict(SIZE_CHOICES).get(identifier)

DEVICE_DICT = {device['identifier']: device for device in DEVICES}

DEVICE_CHOICES = (
    ('xs', _("Tiny")),
    ('sm', _("Small")),
    ('md', _("Medium")),
    ('lg', _("Large")),
)
DEVICE_SIZES = tuple([size for size, name in DEVICE_CHOICES])

GRID_SIZE = settings.ALDRYN_BOOTSTRAP3_GRID_SIZE


ASPECT_RATIOS = (
    (4, 3),
    (16, 9),
    (16, 10),
    (21, 9),
)
ASPECT_RATIOS_REVERSED = tuple([(y, x) for x, y in ASPECT_RATIOS])

ASPECT_RATIO_CHOICES = (
    tuple([
        ('{0}x{1}'.format(1, 1), '{0}x{1}'.format(1, 1))
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS
    ]) + tuple([
        ('{0}x{1}'.format(x, y), '{0}x{1}'.format(x, y))
        for x, y in ASPECT_RATIOS_REVERSED
    ]))
