from django.utils.translation import gettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_bootstrap5.constants import DEVICE_SIZES
from djangocms_bootstrap5.helpers import concat_classes

from .forms import Bootstrap5GridColumnForm, Bootstrap5GridRowForm
from .models import (
    Bootstrap5GridColumn, Bootstrap5GridContainer, Bootstrap5GridRow,
)


class Bootstrap5GridContainerPlugin(CMSPluginBase):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/5.0/layout/grid/
    """
    model = Bootstrap5GridContainer
    name = _('Container')
    module = _('Bootstrap 5')
    render_template = 'djangocms_bootstrap5/grid_container.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'container_type',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        classes = concat_classes([
            instance.container_type,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


class Bootstrap5GridRowPlugin(CMSPluginBase):
    """
    Layout > Grid: "Row" Plugin
    https://getbootstrap.com/docs/5.0/layout/grid/
    """
    model = Bootstrap5GridRow
    name = _('Row')
    module = _('Bootstrap 5')
    form = Bootstrap5GridRowForm
    change_form_template = 'djangocms_bootstrap5/admin/grid_row.html'
    render_template = 'djangocms_bootstrap5/grid_row.html'
    allow_children = True
    child_classes = ['Bootstrap5GridColumnPlugin']

    fieldsets = [
        (None, {
            'fields': (
                'create',
                ('vertical_alignment', 'horizontal_alignment'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                ('tag_type', 'gutters',),
                'attributes',
            )
        }),
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in range(int(data['create']) if data['create'] is not None else 0):
            extra = {}
            for size in DEVICE_SIZES:
                extra['{}_col'.format(size)] = data.get(
                    'create_{}_col'.format(size)
                )
            col = Bootstrap5GridColumn(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=obj.numchild,
                plugin_type=Bootstrap5GridColumnPlugin.__name__,
                **extra
            )
            obj.add_child(instance=col)

    def render(self, context, instance, placeholder):
        gutter = 'no-gutters' if instance.gutters else ''
        classes = concat_classes([
            'row',
            instance.vertical_alignment,
            instance.horizontal_alignment,
            gutter,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = classes

        return super().render(
            context, instance, placeholder
        )


class Bootstrap5GridColumnPlugin(CMSPluginBase):
    """
    Layout > Grid: "Column" Plugin
    https://getbootstrap.com/docs/5.0/layout/grid/
    """
    model = Bootstrap5GridColumn
    name = _('Column')
    module = _('Bootstrap 5')
    form = Bootstrap5GridColumnForm
    change_form_template = 'djangocms_bootstrap5/admin/grid_column.html'
    render_template = 'djangocms_bootstrap5/grid_column.html'
    allow_children = True
    require_parent = True
    # TODO it should allow for the responsive utilitiy class
    # https://getbootstrap.com/docs/5.0/layout/grid/#column-resets
    parent_classes = ['Bootstrap5GridRowPlugin']

    fieldsets = [
        (None, {
            'fields': (
                ('column_type', 'column_alignment'),
            )
        }),
        (_('Responsive settings'), {
            'fields': (
                ['{}_col'.format(size) for size in DEVICE_SIZES],
                ['{}_order'.format(size) for size in DEVICE_SIZES],
                ['{}_offset'.format(size) for size in DEVICE_SIZES],
                ['{}_ml'.format(size) for size in DEVICE_SIZES],
                ['{}_mr'.format(size) for size in DEVICE_SIZES],
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'tag_type',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        column = ''
        classes = instance.get_grid_values()

        if classes:
            column += '{}'.format(' '.join(cls for cls in classes if cls))

        attr_classes = concat_classes([
            instance.column_type,
            column,
            instance.column_alignment,
            instance.attributes.get('class'),
        ])
        instance.attributes['class'] = attr_classes

        return super().render(
            context, instance, placeholder
        )


plugin_pool.register_plugin(Bootstrap5GridContainerPlugin)
plugin_pool.register_plugin(Bootstrap5GridRowPlugin)
plugin_pool.register_plugin(Bootstrap5GridColumnPlugin)
