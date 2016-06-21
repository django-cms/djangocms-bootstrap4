# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import warnings

from django.conf.urls import patterns, url
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

try:
    from filer.admin.clipboardadmin import ajax_upload as filer_ajax_upload
except ImportError:
    filer_ajax_upload = None
    warnings.warn("Drag and drop functionality is not avalable. "
                  "Please update to django-filer>=1.1.1",
                  Warning)

from . import models, forms, constants

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


#################
# Basic Plugins #
#################


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    model = models.Boostrap3BlockquotePlugin
    name = _("Blockquote")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True


plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)


class Bootstrap3IconCMSPlugin(CMSPluginBase):
    model = models.Boostrap3IconPlugin
    name = _("Icon")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/icon.html'
    text_enabled = True

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

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/icon.png')


plugin_pool.register_plugin(Bootstrap3IconCMSPlugin)


class Bootstrap3LabelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3LabelPlugin
    name = _("Label")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/label/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/label.html'
    text_enabled = True

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

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/label.png')


plugin_pool.register_plugin(Bootstrap3LabelCMSPlugin)


class Bootstrap3WellCMSPlugin(CMSPluginBase):
    model = models.Boostrap3WellPlugin
    name = _("Well")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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


plugin_pool.register_plugin(Bootstrap3WellCMSPlugin)


class Bootstrap3AlertCMSPlugin(CMSPluginBase):
    model = models.Boostrap3AlertPlugin
    name = _("Alert")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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
                'txt_context',
                'btn_size',
                'btn_block',
                'icon_left',
                'icon_right',
            ),
        }),
    ) + link_fieldset + (
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'link_attributes',
                # 'responsive',
                # 'responsive_print',
            )
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/button.png')


plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)


class Bootstrap3ImageCMSPlugin(CMSPluginBase):
    model = models.Boostrap3ImagePlugin
    name = _("Image")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/image.html'
    text_enabled = True

    fieldsets = (
        (None, {'fields': (
                'file',
                'use_original_image',
                'aspect_ratio',
                'shape',
                'thumbnail',
                'alt',
        )}),

        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'title',
                'override_width',
                'override_height',
                'classes',
                'img_responsive',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        if callable(filer_ajax_upload):
            # Use this in template to conditionally enable drag-n-drop.
            context.update({'has_dnd_support': True})
        return context

    def get_thumbnail(self, instance):
        return instance.file.file.get_thumbnail({
            'size': (40, 40),
            'crop': True,
            'upscale': True,
            'subject_location': instance.file.subject_location,
        })

    def icon_src(self, instance):
        if instance.file_id:
            thumbnail = self.get_thumbnail(instance)
            return thumbnail.url
        return ''

    def get_plugin_urls(self):
        urlpatterns = patterns(
            '',
            url(r'^ajax_upload/(?P<pk>[0-9]+)/$', self.ajax_upload,
                name='bootstrap3_image_ajax_upload'),
        )
        return urlpatterns

    @csrf_exempt
    def ajax_upload(self, request, pk):

        """
        Handle drag-n-drop uploads.

        Call original 'ajax_upload' Filer view, parse response and update
        plugin instance file_id from it. Send original response back.
        """
        if not callable(filer_ajax_upload):
            # Do not try to handle request if we were unable to
            # import Filer view.
            raise ImproperlyConfigured(
                "Please, use django-filer>=1.1.1 to get drag-n-drop support")
        filer_response = filer_ajax_upload(request, folder_id=None)

        if filer_response.status_code != 200:
            return filer_response

        try:
            file_id = json.loads(filer_response.content)['file_id']
        except ValueError:
            return HttpResponse(
                json.dumps(
                    {'error': 'received non-JSON response from Filer'}),
                status=500,
                content_type='application/json')
        instance = self.model.objects.get(pk=pk)
        instance.file_id = file_id
        instance.save()
        return filer_response

plugin_pool.register_plugin(Bootstrap3ImageCMSPlugin)


class Bootstrap3SpacerCMSPlugin(CMSPluginBase):
    model = models.Boostrap3SpacerPlugin
    name = _("Spacer")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/spacer.html'
    text_enabled = True

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

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/spacer.png')


plugin_pool.register_plugin(Bootstrap3SpacerCMSPlugin)


class Bootstrap3FileCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3FilePlugin
    name = _("File")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/file.html'
    text_enabled = True

    fieldsets = (
        (None, {'fields': (
            'file',
            'name',
            'icon_left',
            'icon_right',
        )}),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'open_new_window',
                'show_file_size',
                'classes',
            ),
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/file.png')


plugin_pool.register_plugin(Bootstrap3FileCMSPlugin)


#########
# Panel #
#########


class Bootstrap3PanelCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelPlugin
    name = _("Panel")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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


plugin_pool.register_plugin(Bootstrap3PanelHeadingCMSPlugin)


class Bootstrap3PanelBodyCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelBodyPlugin
    name = _("Panel Body")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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


plugin_pool.register_plugin(Bootstrap3PanelBodyCMSPlugin)


class Bootstrap3PanelFooterCMSPlugin(CMSPluginBase):
    model = models.Boostrap3PanelFooterPlugin
    name = _("Panel Footer")
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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


plugin_pool.register_plugin(Bootstrap3PanelFooterCMSPlugin)


########
# Grid #
########


class Bootstrap3RowCMSPlugin(CMSPluginBase):
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
            'classes': ('collapse',),
            'fields': (
                'classes',
            )
        }),
    ]

    def save_model(self, request, obj, form, change):
        response = super(Bootstrap3RowCMSPlugin, self).save_model(request, obj, form, change)
        data = form.cleaned_data
        for x in range(int(data['create']) if data['create'] is not None else 0):
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


class Bootstrap3ColumnCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3ColumnPlugin
    name = _('Column')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/plugins/column/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/column.html'
    allow_children = True
    parent_classes = ['Bootstrap3RowCMSPlugin']
    form = forms.ColumnPluginForm

    fieldsets = [
        ("Adapt Columns", {
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


class Bootstrap3AccordionCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3AccordionPlugin
    name = _('Accordion')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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
        context['accordion'] = instance
        context['accordion_id'] = "plugin-bootstrap3-accordion-%s" % instance.pk
        return context


class Bootstrap3AccordionItemCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3AccordionItemPlugin
    name = _('Accordion item')
    module = _('Accordion')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/accordion_item.html'
    allow_children = True
    parent_classes = ['Bootstrap3AccordionCMSPlugin']

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
        context['item'] = instance
        return context


plugin_pool.register_plugin(Bootstrap3AccordionCMSPlugin)
plugin_pool.register_plugin(Bootstrap3AccordionItemCMSPlugin)


#############
# ListGroup #
#############


class Bootstrap3ListGroupCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3ListGroupPlugin
    name = _('List Group')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
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


class Bootstrap3ListGroupItemCMSPlugin(CMSPluginBase):
    model = models.Bootstrap3ListGroupItemPlugin
    name = _('List Group Item')
    module = _('Bootstrap3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/list_group_item.html'
    allow_children = True
    parent_classes = [
        'Bootstrap3ListGroupCMSPlugin',
        'Bootstrap3PanelCMSPlugin',
    ]

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
        context['item'] = instance
        return context


plugin_pool.register_plugin(Bootstrap3ListGroupCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ListGroupItemCMSPlugin)


############
# Carousel #
############


# Base Classes
class CarouselBase(CMSPluginBase):
    module = _('Bootstrap3')


class CarouselSlideBase(CarouselBase):
    require_parent = True
    parent_classes = ['Bootstrap3CarouselCMSPlugin']

    def render(self, context, instance, placeholder):
        # get style from parent plugin, render chosen template
        context['instance'] = instance
        context['image'] = instance.image
        return context

    def get_slide_template(self, instance, name='slide'):
        if instance.parent is None:
            style = models.Bootstrap3CarouselPlugin.STYLE_DEFAULT
        else:
            style = getattr(
                instance.parent.get_plugin_instance()[0],
                'style',
                models.Bootstrap3CarouselPlugin.STYLE_DEFAULT,
            )
        return 'aldryn_bootstrap3/plugins/carousel/{}/{}.html'.format(
            style, name)

    def get_render_template(self, context, instance, placeholder):
        return self.get_slide_template(instance=instance)


# Plugins
class Bootstrap3CarouselCMSPlugin(CarouselBase):
    name = _('Carousel')
    model = models.Bootstrap3CarouselPlugin
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = False
    form = forms.CarouselPluginForm
    allow_children = True
    child_classes = [
        'Bootstrap3CarouselSlideCMSPlugin',
        # 'Bootstrap3CarouselSlideFolderCMSPlugin',
    ]
    fieldsets = (
        (None, {
            'fields': (
                'style',
                'transition_effect',
                ('ride', 'interval'),
                'aspect_ratio',

            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'pause',
                'wrap',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        if instance.child_plugin_instances:
            number_of_slides = sum([
                plugin.folder.file_count
                if isinstance(plugin, Bootstrap3CarouselCMSPlugin) else 1
                for plugin in instance.child_plugin_instances
            ])
        else:
            number_of_slides = 0
        context['slides'] = range(number_of_slides)
        return context

    def get_render_template(self, context, instance, placeholder):
        return 'aldryn_bootstrap3/plugins/carousel/{}/carousel.html'.format(
            instance.style)


carousel_link_fieldset = link_fieldset


class Bootstrap3CarouselSlideCMSPlugin(CarouselSlideBase):
    form = forms.CarouselSlidePluginForm
    model = models.Bootstrap3CarouselSlidePlugin
    name = _('Carousel Slide')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    allow_children = True
    fieldsets = (
        (None, {
            'fields': (
                'image',
                'content',
            )
        }),
    ) + link_fieldset + (
        (_('Link Text'), {
            'fields': (
                'link_text',
            )
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'link_attributes',
            ),
        }),
    )


class Bootstrap3CarouselSlideFolderCMSPlugin(CarouselSlideBase):
    """
    Slide Plugin that renders a slide for each image in the linked folder.
    """
    name = _('Carousel Slides Folder')
    model = models.Bootstrap3CarouselSlideFolderPlugin

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['slide_template'] = self.get_slide_template(
            instance=instance,
            name='image_slide',
        )
        return context

    def get_render_template(self, context, instance, placeholder):
        return self.get_slide_template(instance=instance, name='slide_folder')


plugin_pool.register_plugin(Bootstrap3CarouselCMSPlugin)
plugin_pool.register_plugin(Bootstrap3CarouselSlideCMSPlugin)
# plugin_pool.register_plugin(Bootstrap3CarouselSlideFolderCMSPlugin)
