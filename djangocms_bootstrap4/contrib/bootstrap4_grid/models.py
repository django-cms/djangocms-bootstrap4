from functools import partial

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext
from enumfields import Enum
from enumfields import EnumField
from six import python_2_unicode_compatible

from djangocms_bootstrap4.constants import DEVICE_SIZES
from djangocms_bootstrap4.fields import AttributesField
from djangocms_bootstrap4.fields import IntegerRangeField
from djangocms_bootstrap4.fields import TagTypeField
from djangocms_bootstrap4.helpers import mark_safe_lazy
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_COLUMN_HORIZONTAL_ALIGNMENT_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_COLUMN_ALIGNMENT_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_COLUMN_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_BACKGROUND
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_HORIZONTAL_SPACING
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_VERTICAL_SPACING_INTERNAL
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_VERTICAL_SPACING_EXTERNAL
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_TYPE
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_CONTAINER_WIDTH_INTERNAL
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_ROW_HORIZONTAL_ALIGNMENT_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_ROW_VERTICAL_ALIGNMENT_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import GRID_SIZE


@python_2_unicode_compatible
class Bootstrap4GridContainer(CMSPlugin):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    name = models.CharField(
        max_length=1024,
        null=True, blank=True,
        help_text=_('Shown only to the admins in the structure mode for better orientation'),
    )
    container_type = EnumField(
        GRID_CONTAINER_TYPE,
        default=GRID_CONTAINER_TYPE.FULL_WIDTH,
        verbose_name=_('External width'),
        max_length=255,
    )
    width = EnumField(
        GRID_CONTAINER_WIDTH_INTERNAL,
        default=GRID_CONTAINER_WIDTH_INTERNAL.FULL_WIDTH,
        verbose_name=_('Width'),
        max_length=255,
    )
    background = EnumField(
        GRID_CONTAINER_BACKGROUND,
        default=GRID_CONTAINER_BACKGROUND.NONE,
        verbose_name=_('Background'),
        max_length=255,
    )
    spacing_vertical_external = EnumField(
        GRID_CONTAINER_VERTICAL_SPACING_EXTERNAL,
        default=GRID_CONTAINER_VERTICAL_SPACING_EXTERNAL.NONE,
        verbose_name=_('Vertical external spacing'),
        max_length=255,
    )
    spacing_vertical_internal = EnumField(
        GRID_CONTAINER_VERTICAL_SPACING_INTERNAL,
        default=GRID_CONTAINER_VERTICAL_SPACING_INTERNAL.NONE,
        verbose_name=_('Vertical internal spacing'),
        max_length=255,
    )
    spacing_horizontal = EnumField(
        GRID_CONTAINER_HORIZONTAL_SPACING,
        default=GRID_CONTAINER_HORIZONTAL_SPACING.NONE,
        verbose_name=_('Horizontal spacing (padding)'),
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self) -> str:
        return str(self.pk)

    def get_short_description(self) -> str:
        desc: str = ''
        if self.name:
            desc += f'{self.name} '

        is_width_selected = self.width != self._meta.get_field('width').get_default()
        is_background_selected = self.background != self._meta.get_field('background').get_default()
        if is_background_selected or is_width_selected:
            desc += '['
            if is_background_selected and is_width_selected:
                desc += f'{self.background}, {self.width}'
            elif is_background_selected:
                desc += str(self.background)
            elif is_width_selected:
                desc += str(self.width)
            desc += ']'

        return desc


class GuttersVertical(Enum):
    NONE = 'none'
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'


class GuttersHorizontal(Enum):
    NONE = 'none'
    SMALL = 'small'
    NORMAL = 'normal'
    LARGE = 'large'
    EXTRA_LARGE = 'extra_large'


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
    gutters_vertical = EnumField(
        GuttersVertical,
        default=GuttersVertical.NONE,
        max_length=32,
        help_text=_("Vertical spacing between the columns inside"),
    )
    gutters = models.BooleanField(
        verbose_name=_('Remove gutters'),
        default=False,
        help_text=_('Removes the horizontal spacing between the columns.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        column_count = len(self.child_plugin_instances or [])
        column_count_str = gettext(
            '(1 column)',
            '(%(count)i columns)',
            column_count
        ) % {'count': column_count}

        return column_count_str


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
        blank=True,
        max_length=255,
    )
    column_alignment = models.CharField(
        verbose_name=_('Vertical alignment'),
        choices=GRID_COLUMN_ALIGNMENT_CHOICES,
        blank=True,
        max_length=255,
    )
    horizontal_alignment = models.CharField(
        verbose_name=_('Horizontal alignment'),
        choices=GRID_COLUMN_HORIZONTAL_ALIGNMENT_CHOICES,
        default=GRID_COLUMN_HORIZONTAL_ALIGNMENT_CHOICES[0][0],
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
