from functools import partial

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ungettext

from cms.models import CMSPlugin

from djangocms_bootstrap4.constants import DEVICE_SIZES
from djangocms_bootstrap4.fields import (
    AttributesField, IntegerRangeField, TagTypeField,
)
from djangocms_bootstrap4.helpers import mark_safe_lazy

from .constants import (
    GRID_COLUMN_ALIGNMENT_CHOICES, GRID_COLUMN_CHOICES, GRID_CONTAINER_CHOICES,
    GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES, GRID_ROW_VERTICAL_ALIGNMENT_CHOICES,
    GRID_SIZE,
)


class Bootstrap4GridContainer(CMSPlugin):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    container_type = models.CharField(
        verbose_name=_('Container type'),
        choices=GRID_CONTAINER_CHOICES,
        default=GRID_CONTAINER_CHOICES[0][0],
        max_length=255,
        help_text=mark_safe_lazy(_(
            'Defines if the grid should use fixed width (<code>.container</code>) '
            'or fluid width (<code>.container-fluid</code>).'
        )),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        for item in GRID_CONTAINER_CHOICES:
            if item[0] == self.container_type:
                text = item[1]
        return '({})'.format(text)


class Bootstrap4GridRow(CMSPlugin):
    """
    Layout > Grid: "Row" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    vertical_alignment = models.CharField(
        verbose_name=_('Vertical alignment'),
        choices=GRID_ROW_VERTICAL_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
        help_text=mark_safe_lazy(_(
            'Read more in the <a href="{link}" target="_blank">documentation</a>.')
                .format(link='https://getbootstrap.com/docs/4.0/layout/grid/#vertical-alignment')
        ),
    )
    horizontal_alignment = models.CharField(
        verbose_name=_('Horizontal alignment'),
        choices=GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
        help_text=mark_safe_lazy(_(
            'Read more in the <a href="{link}" target="_blank">documentation</a>.')
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
        column_count = len(self.child_plugin_instances or [])
        column_count_str = ungettext(
            '(1 column)',
            '(%(count)i columns)',
            column_count
        ) % {'count': column_count}

        return column_count_str


class Bootstrap4GridColumn(CMSPlugin):
    """
    Layout > Grid: "Column" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    column_type = models.CharField(
        verbose_name=_('Column type'),
        choices=GRID_COLUMN_CHOICES,
        default=GRID_COLUMN_CHOICES[0][0],
        blank=True,
        max_length=255,
    )
    column_alignment = models.CharField(
        verbose_name=_('Alignment'),
        choices=GRID_COLUMN_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        classes = self.get_grid_values()
        if self.xs_col:
            text += '(col-{}) '.format(self.xs_col)
        else:
            text += '(auto) '
        if self.column_type != 'col':
            text += '.{} '.format(self.column_type)
        if classes:
            text += '.{}'.format(' .'.join(self.get_grid_values()))
        return text

    def get_grid_values(self):
        classes = []
        for device in DEVICE_SIZES:
            for element in ('col', 'order', 'offset', 'ml', 'mr'):
                size = getattr(self, '{}_{}'.format(device, element))
                if isinstance(size, int) and (element == 'col' or element == 'order' or element == 'offset'):
                    if device == 'xs':
                        classes.append('{}-{}'.format(element, int(size)))
                    else:
                        classes.append('{}-{}-{}'.format(element, device, int(size)))
                elif size:
                    if device == 'xs':
                        classes.append('{}-{}'.format(element, 'auto'))
                    else:
                        classes.append('{}-{}-{}'.format(element, device, 'auto'))

        return classes


IntegerRangeFieldPartial = partial(
    IntegerRangeField,
    blank=True,
    null=True,
    max_value=GRID_SIZE,
)

BooleanFieldPartial = partial(
    models.BooleanField,
    default=False,
)

# Loop through Bootstrap 4 device choices and generate
# model fields to cover col-*, order-*, offset-*, etc.
for size in DEVICE_SIZES:
    # Grid size
    Bootstrap4GridColumn.add_to_class(
        '{}_col'.format(size),
        IntegerRangeFieldPartial(),
    )
    # Grid ordering
    Bootstrap4GridColumn.add_to_class(
        '{}_order'.format(size),
        IntegerRangeFieldPartial(),
    )
    # Grid offset
    Bootstrap4GridColumn.add_to_class(
        '{}_offset'.format(size),
        IntegerRangeFieldPartial(),
    )
    # Grid margin left (ml)
    Bootstrap4GridColumn.add_to_class(
        '{}_ml'.format(size),
        BooleanFieldPartial(),
    )
    # Grid margin right (ml)
    Bootstrap4GridColumn.add_to_class(
        '{}_mr'.format(size),
        BooleanFieldPartial(),
    )
