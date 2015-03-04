# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _
import django.forms.widgets

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models, forms, constants, widgets
from cms.models import CMSPlugin


link_fieldset = (
    ('Link', {
        'fields': (
            'page_link', 'file', 'url', 'mailto', 'phone',
        ),
        'description': 'Choose one of the link types below.',
    }),
    ('Link options', {
        'fields': (
            ('target', 'anchor',),
        ),
    }),
)


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    model = models.Boostrap3BlockquotePlugin
    name = _("Blockquote")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/blockquote/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3IconCMSPlugin(CMSPluginBase):
    model = models.Boostrap3IconPlugin
    name = _("Icon")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/icon/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/icon.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'icon',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3IconCMSPlugin)


class Bootstrap3LabelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3LabelPlugin
    name = _("Label")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/label/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/label.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'label',
            'context',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3LabelCMSPlugin)


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ButtonPlugin
    name = _("Link/Button")
    module = _('Bootstrap3')
    form = forms.LinkForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/button/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'type',
                'btn_context',
                'btn_size',
                'btn_block',
                'txt_context',
                'icon_left',
                'icon_right',
            ),
        }),
    ) + link_fieldset + (
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            )
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

    def icon_src(self, instance):
        from django.contrib.staticfiles.templatetags.staticfiles import static
        return static("cms/img/icons/plugins/link.png")

plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)


class Bootstrap3ImageCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ImagePlugin
    name = _("Image")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/image/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/image.html'
    allow_children = True
    cache = False

    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'label',
    #             'context',
    #             'size',
    #             'icon_left',
    #             'icon_right',
    #         )
    #     }),
    # ) + link_fieldset + (
    #     ('Advanced', {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'classes',
    #         )
    #     }),
    # )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3ImageCMSPlugin)


#########
# Panel #
#########


class Bootstrap3PanelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelPlugin
    name = _("Panel")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel.html'
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'context',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelCMSPlugin)


class Bootstrap3PanelHeadingCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelHeadingPlugin
    name = _("Panel Heading")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_heading/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_heading.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        (None, {'fields': (
            'title',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelHeadingCMSPlugin)


class Bootstrap3PanelBodyCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PabelBodyPlugin
    name = _("Panel Body")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_body/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_body.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        # (None, {'fields': (
        #     'title',
        # )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelBodyCMSPlugin)


class Bootstrap3PanelFooterCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelFooterPlugin
    name = _("Panel Footer")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_footer/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_footer.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        # (None, {'fields': (
        #     'title',
        # )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(Bootstrap3PanelFooterCMSPlugin)


########
# Grid #
########


class Bootstrap3RowCMSPlugin(widgets.BootstrapMediaMixin, CMSPluginBase):
    model = models.Bootstrap3RowPlugin
    name = _('Row')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/row/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/row.html'
    allow_children = True
    child_classes = ['Bootstrap3ColumnCMSPlugin']
    form = forms.RowPluginForm
    fieldsets = [
        ("Create Columns", {
            # 'classes': ('collapse',),
            'fields': (
                'create',
            ) + tuple([
                (
                    'create_{}_col'.format(size),
                    'create_{}_offset'.format(size),
                    'create_{}_push'.format(size),
                    'create_{}_pull'.format(size),
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
                for element in ['col', 'offset', 'push', 'pull']:
                    extra['{}_{}'.format(size, element)] = data.get(
                        'create_{}_{}'.format(size, element)) or None
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


class Bootstrap3ColumnCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3ColumnPlugin
    name = _('Column')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/column/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/column.html'
    allow_children = True
    parent_classes = ['Bootstrap3RowCMSPlugin']

    fieldsets = [
        (None, {
            'fields': tuple([
                (
                    '{}_col'.format(size),
                    '{}_offset'.format(size),
                    '{}_push'.format(size),
                    '{}_pull'.format(size),
                ) for size in constants.DEVICE_SIZES
            ])
        }),
        ("Advanced", {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'tag',
            )
        }),
    ]


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
