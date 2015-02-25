# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models, forms, constants
from cms.models import CMSPlugin


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    model = models.Boostrap3BlockquotePlugin
    name = _("Blockquote")
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ButtonPlugin
    name = _("Button")
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    allow_children = True
    readonly_fields = (
        'preview',
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def preview(self, **kwargs):
        from django.template.loader import render_to_string
        rendered = render_to_string('aldryn_bootstrap3/plugins/button_admin_preview.html', {})
        return rendered
    preview.allow_tags = True

plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)


########
# Grid #
########


class Bootstrap3RowCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3RowPlugin
    name = _('Row')
    module = _('Grid')
    render_template = 'aldryn_bootstrap3/plugins/row.html'
    allow_children = True
    # child_classes = ['Bootstrap3Column']
    form = forms.RowPluginForm
    fieldsets = [
        ("Create Columns", {
            'classes': ('collapse',),
            'fields': (
                'create',
            ) + tuple([
                (
                    'create_{}_size'.format(size),
                    'create_{}_offset'.format(size)
                ) for size in constants.DEVICE_SIZES
            ])
        }),
        ("Advanced", {
            'fields': (
                'classes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3RowCMSPlugin, self).render(context, instance, placeholder)
        return context

    def save_model(self, request, obj, form, change):
        response = super(Bootstrap3RowCMSPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in xrange(int(data['create']) if data['create'] is not None else 0):
            extra = {}
            for size in constants.DEVICE_SIZES:
                extra['{}_size'.format(size)] = data.get('create_{}_size'.format(size)) or None
                extra['{}_offset'.format(size)] = data.get('create_{}_offset'.format(size)) or None
            col = models.Bootstrap3ColumnPlugin(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=Bootstrap3ColumnCMSPlugin.__name__,
                **extra
            )
            col.save()
        return response


class Bootstrap3ColumnCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3ColumnPlugin
    name = _('Column')
    module = _('Grid')
    render_template = 'aldryn_bootstrap3/plugins/column.html'
    allow_children = True


plugin_pool.register_plugin(Bootstrap3RowCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ColumnCMSPlugin)




# Boostrap3AppdataPluginMultiform = app_data.multiform_factory(forms.Bootstrap3AppDataForm)


# class Bootstrap3AppdataCMSPlugin(app_data.admin.AppDataAdminMixin, CMSPluginBase):
#     model = Bootstrap3AppdataPlugin
#     name = _("My Appdata Plugin")
#     render_template = 'aldryn_bootstrap3/plugins/button.html'
#     allow_children = True
#     # multiform = Boostrap3AppdataPluginMultiform
#
#     declared_fieldsets = [
#         (None, {'fields': ['label', 'url',]}),
#         ('Bootstrap', {'fields': [('bootstrap3.breakpoints', 'bootstrap3.button_size', 'bootstrap3.button_types')]})
#     ]
#
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
#
#     def get_form(self, request, obj=None, **kwargs):
#         """
#         Returns a Form class for use in the admin add view. This is used by
#         add_view and change_view.
#         """
#         if self.multiform is None:
#             return super(Bootstrap3AppdataCMSPlugin, self).get_form(request, obj=obj, **kwargs)
#         return app_data.forms.multiform_factory(self.model, **self._get_form_factory_opts(request, obj, **kwargs))
#
# plugin_pool.register_plugin(Bootstrap3AppdataCMSPlugin)


# class BootstrapContainerCMSPlugin(CMSPluginBase):
#     model = BootstrapContainerPlugin
#     name = _("Responsive Wrapper")
#     render_template = 'aldryn_responsive/plugins/wrapper.html'
#     allow_children = True
#
#     def render(self, context, instance, placeholder):
#         context.update({'instance': instance})
#         return context
#
# plugin_pool.register_plugin(ResponsiveWrapperCMSPlugin)
