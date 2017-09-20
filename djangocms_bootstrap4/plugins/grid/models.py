# -*- coding: utf-8 -*-
from functools import partial

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.safestring import mark_safe

from cms.models import CMSPlugin

from ...utils import TagTypeField, AttributesField, IntegerRangeField
from ...constants import DEVICE_CHOICES


# The default grid size for Bootstrap 4 is 12. You can change this setting
# to whatever layout you require. We suggest that the value is at
# least devisable by 2, 3 and 4.
GRID_SIZE = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_SIZE',
    12,
)

# Bootstrap 4 provides 2 container types, .container and .container-fluid
# https://getbootstrap.com/docs/4.0/layout/grid/#no-gutters
GRID_CONTAINERS = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS',
    (
        ('container', _('Fixed width')),
        ('container-fluid', _('Full width')),
    ),
)

# Options for flexbox on the alignment of the grid
# https://flexbox.webflow.com/
GRID_ROW_VERTICAL_ALIGNMENT = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_ROW_VERTICAL_ALIGNMENT',
    (
        ('align-items-start', _('Top')),
        ('align-items-center', _('Middle')),
        ('align-items-end', _('Bottom')),
    ),
)

GRID_ROW_HORIZONTAL_ALIGNMENT = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_ROW_HORIZONTAL_ALIGNMENT',
    (
        ('justify-content-start', _('Justify left')),
        ('justify-content-end', _('Justify right')),
        ('justify-content-center', _('Justify center')),
        ('justify-content-around', _('Justify center with space around')),
        ('justify-content-between', _('Justify center with space in-between')),
    ),
)

GRID_COLUMN_CHOICES = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES',
    (
        ('col', _('Column')),
        ('w-100', _('Break')),
    ),
)

GRID_COLUMN_ALIGNMENT = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_ALIGNMENT',
    (
        ('align-self-start', _('Left')),
        ('align-self-center', _('Center')),
        ('align-self-end', _('Right')),
    ),
)


@python_2_unicode_compatible
class Bootstrap4GridContainer(CMSPlugin):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    container_type = models.CharField(
        verbose_name=_('Container type'),
        choices=GRID_CONTAINERS,
        default=GRID_CONTAINERS[0][0],
        max_length=255,
        help_text=_(mark_safe(
            'Defines if the grid should use fixed width (<code>.container</code>) '
            'or fluid width (<code>.container-fluid</code>).'
        )),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        text = ''
        for item in GRID_CONTAINERS:
            if item[0] == self.container_type:
                text = item[1]
        return str('({})'.format(text))


# TODO add create field for columns
@python_2_unicode_compatible
class Bootstrap4GridRow(CMSPlugin):
    """
    Layout > Grid: "Row" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    vertical_alignment = models.CharField(
        verbose_name=_('Vertical alignment'),
        choices=GRID_ROW_VERTICAL_ALIGNMENT,
        blank=True,
        max_length=255,
        help_text=mark_safe(
            _('Read more in the <a href="{link}" target="_blank">documentation</a>.')
                .format(link='https://getbootstrap.com/docs/4.0/layout/grid/#vertical-alignment')
        ),
    )
    horizontal_alignment = models.CharField(
        verbose_name=_('Horizontal alignment'),
        choices=GRID_ROW_HORIZONTAL_ALIGNMENT,
        blank=True,
        max_length=255,
        help_text=mark_safe(
            _('Read more in the <a href="{link}" target="_blank">documentation</a>.')
                .format(link='https://getbootstrap.com/docs/4.0/layout/grid/#horizontal-alignment')
        ),
    )
    gutters = models.BooleanField(
        verbose_name=_('Remove gutters'),
        default=False,
        help_text=_('Removes the marginal gutters from the grid.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        instance = self.get_plugin_instance()[0]

        if not instance:
            return ugettext('<empty>')

        column_count = len(self.child_plugin_instances or [])
        column_count_str = ungettext(
            '1 column',
            '%(count)i columns',
            column_count
        ) % {'count': column_count}

        if self.classes:
            return '{} ({})'.format(
                self.classes,
                column_count_str
            )
        return column_count_str


"""
Simple mode
    Type:
        - col
        - w-100 (for break)
    Size (optional):
        - number (1-12) grid setting
    Breakpoint start (optional):
        - default, xs, sm, md, lg, xl
        > converts to col-md-*
    Alignment (optional)
        - align-self-start, align-self-center, align-self-end

Responsive
    Offset:
        (margin right, margin-left)
        ml-auto, ml-md-auto...
        mr-auto, mr-md-auto...
    Ordering:
        order-1, (numbers 1-12) order-md-1...
    Responsive:
        xs, sm, md, lg, xl with numbers 1-12

"""
@python_2_unicode_compatible
class Bootstrap4GridColumn(CMSPlugin):
    """
    Layout > Grid: "Column" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    column_type = models.CharField(
        verbose_name=_('Column type'),
        choices=GRID_COLUMN_CHOICES,
        default=GRID_COLUMN_CHOICES[0][0],
        max_length=255,
    )
    column_size = IntegerRangeField(
        verbose_name=_('Columne size'),
        blank=True,
        null=True,
        min_value=0,
        max_value=GRID_SIZE,
        help_text=_(
            'Nummeric value from 1 - {bound}. '
            'Spreads the columns evenly when empty.').format(bound=GRID_SIZE)
    )
    column_alignment = models.CharField(
        verbose_name=_('Column alignment'),
        choices=GRID_COLUMN_ALIGNMENT,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        text = ' '.join([self.get_column_classes()])
        if self.tag != 'div':
            text = '{} ({})'.format(text, self.tag)
        return text

    def get_class(self, device, element):
        size = getattr(self, '{}_{}'.format(device, element), None)
        if size is not None:
            if element == 'col':
                return 'col-{}-{}'.format(device, size)
            else:
                return 'col-{}-{}-{}'.format(device, element, size)
        return ''

    def get_column_classes(self):
        classes = []
        for device in DEVICE_SIZES:
            for element in ('col', 'offset', 'push', 'pull'):
                classes.append(self.get_class(device, element))
        return ' '.join(cls for cls in classes if cls)


IntegerRangeFieldPartial = partial(
    IntegerRangeField,
    blank=True,
    null=True,
    min_value=0,
    max_value=GRID_SIZE,
)

BooleanFieldPartial = partial(
    models.BooleanField,
    default=False,
)

# Loop through Bootstrap 4 device choices and generate
# model fields to cover col-*, order-*
for size, name in DEVICE_CHOICES:
    # Grid size
    Bootstrap4GridColumn.add_to_class(
        '{}_col'.format(size),
        IntegerRangeFieldPartial(
            verbose_name='col-{}'.format(size),
        ),
    )
    # Grid auto alignment
    Bootstrap4GridColumn.add_to_class(
        '{}_auto'.format(size),
        BooleanFieldPartial(
            verbose_name='col-auto-{}'.format(size),
        ),
    )
    # Grid ordering
    Bootstrap4GridColumn.add_to_class(
        '{}_order'.format(size),
        IntegerRangeFieldPartial(
            verbose_name='order-{}'.format(size),
        ),
    )
    # Grid margin left (ml)
    Bootstrap4GridColumn.add_to_class(
        '{}_ml'.format(size),
        BooleanFieldPartial(
            verbose_name='ml-{}'.format(size),
        ),
    )
    # Grid margin right (ml)
    Bootstrap4GridColumn.add_to_class(
        '{}_mr'.format(size),
        BooleanFieldPartial(
            verbose_name='mr-{}'.format(size),
        ),
    )
