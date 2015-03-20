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
            'link_page', 'link_file', 'link_url', 'link_mailto', 'link_phone',
        ),
        'description': 'Choose one of the link types below.',
    }),
    ('Link options', {
        'fields': (
            ('link_target', 'link_anchor',),
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


class Bootstrap3WellCMSPlugin(CMSPluginBase):
    model = models.Boostrap3WellPlugin
    name = _("Well")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/well/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/well.html'
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'size',
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


plugin_pool.register_plugin(Bootstrap3WellCMSPlugin)


class Bootstrap3AlertCMSPlugin(CMSPluginBase):
    model = models.Boostrap3AlertPlugin
    name = _("Alert")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/alert/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/alert.html'
    allow_children = True

    fieldsets = (
        (None, {'fields': (
            'context',
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


plugin_pool.register_plugin(Bootstrap3AlertCMSPlugin)


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
                # 'responsive',
                # 'responsive_print',
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


class Bootstrap3ImageCMSPlugin(widgets.BootstrapMediaMixin, CMSPluginBase):
    model = models.Boostrap3ImagePlugin
    name = _("Image")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/image/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/image.html'
    allow_children = True
    cache = False

    fieldsets = (
        (None, {'fields': (
                'file',
                'aspect_ratio',
                'shape',
                'thumbnail',
                'alt',
        )}),

        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'classes',
                'img_responsive',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


plugin_pool.register_plugin(Bootstrap3ImageCMSPlugin)


class Bootstrap3SpacerCMSPlugin(CMSPluginBase):
    model = models.Boostrap3SpacerPlugin
    name = _("Spacer")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/spacer/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/spacer.html'

    fieldsets = (
        (None, {'fields': (
            'size',
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


plugin_pool.register_plugin(Bootstrap3SpacerCMSPlugin)


# ########
# Panel #
# ########


class Bootstrap3PanelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelPlugin
    name = _("Panel")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel.html'
    form = forms.PanelPluginBaseForm
    allow_children = True

    fieldsets = (
        ('Create', {
            'fields': (
                ('create_heading', 'create_body', 'create_footer'),
            )
        }),
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

    def save_model(self, request, obj, form, change):
        response = super(Bootstrap3PanelCMSPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        extra = {}
        subplugins = (
            ('create_heading', models.Boostrap3PanelHeadingPlugin, Bootstrap3PanelHeadingCMSPlugin),
            ('create_body', models.Boostrap3PanelBodyPlugin, Bootstrap3PanelBodyCMSPlugin),
            ('create_footer', models.Boostrap3PanelFooterPlugin, Bootstrap3PanelFooterCMSPlugin),
        )
        existing_plugins = [p.plugin_type for p in obj.get_children()]
        for field, model_class, plugin_class in subplugins:
            if not data.get(field):
                # TODO: delete?
                continue
            if plugin_class.__name__ in existing_plugins:
                continue
            plugin = model_class(
                parent=obj,
                placeholder=obj.placeholder,
                language=obj.language,
                position=CMSPlugin.objects.filter(parent=obj).count(),
                plugin_type=plugin_class.__name__,
                **extra
            )
            plugin.save()
        return response


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
    model = models.Boostrap3PanelBodyPlugin
    name = _("Panel Body")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/panel_body/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_body.html'
    allow_children = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        # (None, {'fields': (
        # 'title',
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
        # 'title',
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


# #######
# Grid #
# #######


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


#############
# Accordion #
#############


class Bootstrap3AccordionCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3AccordionPlugin
    name = _('Accordion')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/accordion/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/accordion.html'
    allow_children = True
    child_classes = ['Bootstrap3AccordionItemCMSPlugin']

    fieldsets = (
        (None, {
            'fields': (
                'index',
            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3AccordionCMSPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        context['accordion'] = instance
        context['accordion_id'] = "plugin-bootstrap3-accordion-%s" % instance.pk
        return context


class Bootstrap3AccordionItemCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3AccordionItemPlugin
    name = _('Accordion item')
    module = _('Accordion')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/accordion_item/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/accordion_item.html'
    allow_children = True
    parent_classes = ['Bootstrap3AccordionCMSPlugin']
    cache = False

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'context',
            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3AccordionItemCMSPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        context['item'] = instance
        return context


plugin_pool.register_plugin(Bootstrap3AccordionCMSPlugin)
plugin_pool.register_plugin(Bootstrap3AccordionItemCMSPlugin)


#############
# ListGroup #
#############


class Bootstrap3ListGroupCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3ListGroupPlugin
    name = _('List Group')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/list_group/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/list_group.html'
    allow_children = True
    child_classes = ['Bootstrap3ListGroupItemCMSPlugin']

    fieldsets = (
        # (None, {
        #     'fields': (
        #         'index',
        #     )
        # }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'add_list_group_class',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3ListGroupCMSPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        return context


class Bootstrap3ListGroupItemCMSPlugin(CMSPluginBase, widgets.BootstrapMediaMixin):
    model = models.Bootstrap3ListGroupItemPlugin
    name = _('List Group Item')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/list_group_item/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/list_group_item.html'
    allow_children = True
    parent_classes = [
        'Bootstrap3ListGroupCMSPlugin',
        'Bootstrap3PanelCMSPlugin',
    ]
    cache = False

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'context',
                'state',
            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3ListGroupItemCMSPlugin, self).render(context, instance, placeholder)
        context['instance'] = instance
        context['item'] = instance
        return context


plugin_pool.register_plugin(Bootstrap3ListGroupCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ListGroupItemCMSPlugin)
