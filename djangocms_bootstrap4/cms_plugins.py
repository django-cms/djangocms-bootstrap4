# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import json
import warnings

from django.conf.urls import url
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
    warnings.warn('Drag and drop functionality is not avalable. '
                  'Please update to django-filer>=1.1.1',
                  Warning)

from . import models, forms, constants


class Bootstrap3RowCMSPlugin(CMSPluginBase):
    """
    CSS - Grid system: "Row" Plugin
    http://getbootstrap.com/css/#grid
    """
    model = models.Bootstrap3RowPlugin
    name = _('Row')
    module = _('Bootstrap 3')
    form = forms.RowPluginForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/row/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/row.html'
    allow_children = True
    child_classes = ['Bootstrap3ColumnCMSPlugin']

    fieldsets = [
        (_('Create columns'), {
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
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
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
                        'create_{}_{}'.format(size, element)
                    )
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
    """
    CSS - Grid system: "Column" Plugin
    http://getbootstrap.com/css/#grid
    """
    model = models.Bootstrap3ColumnPlugin
    name = _('Column')
    module = _('Bootstrap 3')
    form = forms.ColumnPluginForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/column/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/column.html'
    allow_children = True
    parent_classes = ['Bootstrap3RowCMSPlugin']

    fieldsets = [
        (_('Adjust columns'), {
            'fields': tuple([
                (
                    '{}_col'.format(size),
                    '{}_offset'.format(size),
                    '{}_push'.format(size),
                    '{}_pull'.format(size),
                ) for size in constants.DEVICE_SIZES
            ])
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
                'tag',
            )
        }),
    ]


class Bootstrap3BlockquoteCMSPlugin(CMSPluginBase):
    """
    CSS - Typography: "Blockquote" Plugin
    http://getbootstrap.com/css/#type-blockquotes
    """
    model = models.Boostrap3BlockquotePlugin
    name = _('Blockquote')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/blockquote.html'
    allow_children = True

    fieldsets = [
        (None, {
            'fields': (
                'reverse',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            )
        }),
    ]


class Bootstrap3CiteCMSPlugin(CMSPluginBase):
    """
    CSS - Typography: "Cite" Plugin
    http://getbootstrap.com/css/#type-blockquotes
    """
    model = models.Boostrap3CitePlugin
    name = _('Cite')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/cite.html'
    allow_children = True
    # even though we can make this accessible by all means, we only want
    # to restrict it to the blockquote plugin for now
    require_parent = True
    parent_classes = ['Bootstrap3BlockquoteCMSPlugin']

    fieldsets = [
        (None, {
            'fields': ()
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            )
        }),
    ]


class Bootstrap3CodeCMSPlugin(CMSPluginBase):
    """
    CSS - Code: Model
    http://getbootstrap.com/css/#code
    """
    model = models.Bootstrap3CodePlugin
    name = _('Code')
    module = _('Bootstrap 3')
    form = forms.Bootstrap3CodePluginForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/code/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/code.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': (
                'code_type',
                'code',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            )
        }),
    )


class Bootstrap3ButtonCMSPlugin(CMSPluginBase):
    """
    CSS - Buttons: "Button/Link" Plugin
    http://getbootstrap.com/css/#buttons
    """
    model = models.Boostrap3ButtonPlugin
    name = _('Link/Button')
    module = _('Bootstrap 3')
    form = forms.LinkForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/button/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/button.html'
    text_enabled = True
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'type',
                'label',
                ('link_url', 'link_page',),
                'btn_context',
                'txt_context',
                'btn_size',
                ('icon_left', 'icon_right', 'btn_block',),
            ),
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link_mailto', 'link_phone'),
                ('link_anchor', 'link_target'),
                'link_file',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'link_attributes',
            )
        }),
    )

    @classmethod
    def get_render_queryset(cls):
        queryset = super(Bootstrap3ButtonCMSPlugin, cls).get_render_queryset()
        return queryset.select_related('link_page')

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/button.png')


class Bootstrap3ImageCMSPlugin(CMSPluginBase):
    """
    CSS - Images: Plugin
    http://getbootstrap.com/css/#images
    """
    model = models.Boostrap3ImagePlugin
    name = _('Image')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/image.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': (
                'file',
                'alt',
                ('use_original_image', 'thumbnail',),
                ('aspect_ratio', 'shape',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'title',
                ('override_width', 'override_height',),
                'img_responsive',
                'classes',
                'attributes',
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
        urlpatterns = [
            url(
                r'^ajax_upload/(?P<pk>[0-9]+)/$',
                self.ajax_upload,
                name='bootstrap3_image_ajax_upload'
            ),
        ]
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
                'Please use django-filer>=1.1.1 to get drag & drop support.'
            )
        filer_response = filer_ajax_upload(request, folder_id=None)

        if filer_response.status_code != 200:
            return filer_response

        try:
            file_id = json.loads(filer_response.content)['file_id']
        except ValueError:
            return HttpResponse(
                json.dumps(
                    {'error': 'Received non-JSON response from django Filer.'}
                ),
                status=500,
                content_type='application/json')
        instance = self.model.objects.get(pk=pk)
        instance.file_id = file_id
        instance.save()
        return filer_response


class Bootstrap3ResponsiveCMSPlugin(CMSPluginBase):
    """
    CSS - Responsive: "Utilities" Plugin
    http://getbootstrap.com/css/#responsive-utilities
    """
    model = models.Bootstrap3ResponsivePlugin
    name = _('Responsive utilities')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/responsive.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'device_breakpoints',
                'print_breakpoints',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3IconCMSPlugin(CMSPluginBase):
    """
    Component - Glyphicons: "Icon" Plugin
    http://getbootstrap.com/components/#glyphicons
    Component - Font Awesome: "Icon" Plugin
    http://fontawesome.io/
    """
    model = models.Boostrap3IconPlugin
    name = _('Icon')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/icon.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': (
                'icon',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/icon.png')


class Bootstrap3LabelCMSPlugin(CMSPluginBase):
    """
    Component - Label: Plugin
    http://getbootstrap.com/components/#labels
    """
    model = models.Boostrap3LabelPlugin
    name = _('Label')
    module = _('Bootstrap 3')
    form = forms.Boostrap3LabelPluginForm
    change_form_template = 'admin/aldryn_bootstrap3/plugins/label/change_form.html'
    render_template = 'aldryn_bootstrap3/plugins/label.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'context',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/label.png')


class Bootstrap3JumbotronCMSPlugin(CMSPluginBase):
    """
    Component - Jumbotron: Plugin
    http://getbootstrap.com/components/#jumbotron
    """
    model = models.Boostrap3JumbotronPlugin
    name = _('Jumbotron')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/jumbotron.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'label',
                'grid',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3AlertCMSPlugin(CMSPluginBase):
    """
    Component - Alert: Plugin
    http://getbootstrap.com/components/#alerts
    """
    model = models.Boostrap3AlertPlugin
    name = _('Alert')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/alert.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'context',
                'icon',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3ListGroupCMSPlugin(CMSPluginBase):
    """
    Component - List group: "Wrapper" Plugin
    http://getbootstrap.com/components/#alerts
    """
    model = models.Bootstrap3ListGroupPlugin
    name = _('List Group')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/list_group.html'
    allow_children = True
    child_classes = ['Bootstrap3ListGroupItemCMSPlugin']

    fieldsets = (
        (None, {
            'fields': (
                'add_list_group_class',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3ListGroupItemCMSPlugin(CMSPluginBase):
    """
    Component - List group: "Item" Plugin
    http://getbootstrap.com/components/#alerts
    """
    model = models.Bootstrap3ListGroupItemPlugin
    name = _('List Group Item')
    module = _('Bootstrap 3')
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
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3ListGroupItemCMSPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context


class Bootstrap3PanelCMSPlugin(CMSPluginBase):
    """
    Component - Panel: "Wrapper" Plugin
    http://getbootstrap.com/components/#panels
    """
    model = models.Boostrap3PanelPlugin
    name = _('Panel')
    module = _('Bootstrap 3')
    form = forms.PanelPluginBaseForm
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/panel.html'
    allow_children = True
    child_classes = [
        'Bootstrap3PanelHeadingCMSPlugin',
        'Bootstrap3PanelBodyCMSPlugin',
        'Bootstrap3PanelFooterCMSPlugin',
    ]

    fieldsets = (
        (_('Create'), {
            'fields': (
                'create_heading',
                'create_body',
                'create_footer',
            )
        }),
        (_('Settings'), {
            'fields': (
                'context',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
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


class Bootstrap3PanelHeadingCMSPlugin(CMSPluginBase):
    """
    Component - Panel: "Heading" Plugin
    http://getbootstrap.com/components/#panels-heading
    """
    model = models.Boostrap3PanelHeadingPlugin
    name = _('Panel header')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_heading.html'
    allow_children = True
    require_parent = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3PanelBodyCMSPlugin(CMSPluginBase):
    """
    Component - Panel: "Body" Plugin
    http://getbootstrap.com/components/#panels
    """
    model = models.Boostrap3PanelBodyPlugin
    name = _('Panel body')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_body.html'
    allow_children = True
    require_parent = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        (None, {
            'fields': ()
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3PanelFooterCMSPlugin(CMSPluginBase):
    """
    Component - Panel: "Footer" Plugin
    http://getbootstrap.com/components/#panels-footer
    """
    model = models.Boostrap3PanelFooterPlugin
    name = _('Panel footer')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/panel_footer.html'
    allow_children = True
    require_parent = True
    parent_classes = ['Bootstrap3PanelCMSPlugin']

    fieldsets = (
        (None, {
            'fields': ()
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3WellCMSPlugin(CMSPluginBase):
    """
    Component - Wells: Plugin
    http://getbootstrap.com/components/#wells
    """
    model = models.Boostrap3WellPlugin
    name = _('Well')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/well.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'size',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3TabCMSPlugin(CMSPluginBase):
    """
    JavaScript - Tab: "Wrapper" Plugin
    http://getbootstrap.com/javascript/#tabs
    """
    model = models.Bootstrap3TabPlugin
    name = _('Tab')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/tab.html'
    allow_children = True
    # TODO add dropdown support once available as plugin
    child_classes = ['Bootstrap3TabItemCMSPlugin']

    fieldsets = (
        (None, {
            'fields': (
                'index',
                ('style', 'effect',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3TabCMSPlugin, self).render(context, instance, placeholder)
        context['tab_plugin'] = instance
        return context


class Bootstrap3TabItemCMSPlugin(CMSPluginBase):
    """
    JavaScript - Tab: "Item" Plugin
    http://getbootstrap.com/javascript/#tabs
    """
    model = models.Bootstrap3TabItemPlugin
    name = _('Tab item')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/tab_item.html'
    allow_children = True
    parent_classes = ['Bootstrap3TabCMSPlugin']

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'icon',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )


class Bootstrap3AccordionCMSPlugin(CMSPluginBase):
    """
    JavaScript - Collapse: "Accordion" Plugin
    http://getbootstrap.com/javascript/#collapse
    """
    model = models.Bootstrap3AccordionPlugin
    name = _('Accordion')
    module = _('Bootstrap 3')
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
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3AccordionCMSPlugin, self).render(context, instance, placeholder)
        context['accordion'] = instance
        context['accordion_id'] = 'plugin-bootstrap3-accordion-{}'.format(instance.pk)
        return context


class Bootstrap3AccordionItemCMSPlugin(CMSPluginBase):
    """
    JavaScript - Collapse: "Accordion item" Plugin
    http://getbootstrap.com/javascript/#collapse
    """
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
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def render(self, context, instance, placeholder):
        context = super(Bootstrap3AccordionItemCMSPlugin, self).render(context, instance, placeholder)
        context['item'] = instance
        return context


class CarouselBase(CMSPluginBase):
    module = _('Bootstrap 3')


class CarouselSlideBase(CarouselBase):
    """
    JavaScript - Carousel: Base Plugin
    http://getbootstrap.com/javascript/#carousel
    """
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
        return 'aldryn_bootstrap3/plugins/carousel/{}/{}.html'.format(style, name)

    def get_render_template(self, context, instance, placeholder):
        return self.get_slide_template(instance=instance)


class Bootstrap3CarouselCMSPlugin(CarouselBase):
    """
    JavaScript - Carousel: "Wrapper" Plugin
    http://getbootstrap.com/javascript/#carousel
    """
    model = models.Bootstrap3CarouselPlugin
    name = _('Carousel')
    form = forms.CarouselPluginForm
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = False
    allow_children = True
    child_classes = [
        'Bootstrap3CarouselSlideCMSPlugin',
        # 'Bootstrap3CarouselSlideFolderCMSPlugin',
    ]
    fieldsets = (
        (None, {
            'fields': (
                'style',
                'interval',
                ('aspect_ratio', 'transition_effect',),
                ('ride', 'pause', 'wrap',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
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
        return 'aldryn_bootstrap3/plugins/carousel/{}/carousel.html'.format(instance.style)


class Bootstrap3CarouselSlideCMSPlugin(CarouselSlideBase):
    """
    JavaScript - Carousel: "Slide" Plugin
    http://getbootstrap.com/javascript/#carousel
    """
    model = models.Bootstrap3CarouselSlidePlugin
    name = _('Carousel slide')
    form = forms.CarouselSlidePluginForm
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    allow_children = True

    fieldsets = (
        (None, {
            'fields': (
                'image',
                'content',
            )
        }),
        (_('Link settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link_url', 'link_page',),
                ('link_mailto', 'link_phone'),
                ('link_anchor', 'link_target'),
                'link_file',
                'link_text',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'link_attributes',
            ),
        }),
    )

    @classmethod
    def get_render_queryset(cls):
        queryset = super(Bootstrap3CarouselSlideCMSPlugin, cls).get_render_queryset()
        return queryset.select_related('link_page')


class Bootstrap3CarouselSlideFolderCMSPlugin(CarouselSlideBase):
    """
    JavaScript - Carousel: "Slide folder" Plugin
    http://getbootstrap.com/javascript/#carousel
    """
    model = models.Bootstrap3CarouselSlideFolderPlugin
    name = _('Carousel slides folder')

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['slide_template'] = self.get_slide_template(
            instance=instance,
            name='image_slide',
        )
        return context

    def get_render_template(self, context, instance, placeholder):
        return self.get_slide_template(instance=instance, name='slide_folder')


class Bootstrap3SpacerCMSPlugin(CMSPluginBase):
    """
    Custom - Spacer: Plugin
    """
    model = models.Boostrap3SpacerPlugin
    name = _('Spacer')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/spacer.html'
    text_enabled = True
    text_editor_preview = False

    fieldsets = (
        (None, {
            'fields': (
                'size',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/spacer.png')


class Bootstrap3FileCMSPlugin(CMSPluginBase):
    """
    Custom - File: Plugin
    """
    model = models.Bootstrap3FilePlugin
    name = _('File')
    module = _('Bootstrap 3')
    change_form_template = 'admin/aldryn_bootstrap3/base.html'
    render_template = 'aldryn_bootstrap3/plugins/file.html'
    text_enabled = True

    fieldsets = (
        (None, {
            'fields': (
                'file',
                'name',
                ('open_new_window', 'show_file_size',),
                ('icon_left', 'icon_right',),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'classes',
                'attributes',
            ),
        }),
    )

    def icon_src(self, instance):
        return static('aldryn_bootstrap3/img/type/file.png')


plugin_pool.register_plugin(Bootstrap3RowCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ColumnCMSPlugin)
plugin_pool.register_plugin(Bootstrap3BlockquoteCMSPlugin)
plugin_pool.register_plugin(Bootstrap3CiteCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ButtonCMSPlugin)
plugin_pool.register_plugin(Bootstrap3CodeCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ImageCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ResponsiveCMSPlugin)
plugin_pool.register_plugin(Bootstrap3IconCMSPlugin)
plugin_pool.register_plugin(Bootstrap3LabelCMSPlugin)
plugin_pool.register_plugin(Bootstrap3JumbotronCMSPlugin)
plugin_pool.register_plugin(Bootstrap3AlertCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ListGroupCMSPlugin)
plugin_pool.register_plugin(Bootstrap3ListGroupItemCMSPlugin)
plugin_pool.register_plugin(Bootstrap3PanelCMSPlugin)
plugin_pool.register_plugin(Bootstrap3PanelHeadingCMSPlugin)
plugin_pool.register_plugin(Bootstrap3PanelBodyCMSPlugin)
plugin_pool.register_plugin(Bootstrap3PanelFooterCMSPlugin)
plugin_pool.register_plugin(Bootstrap3WellCMSPlugin)
plugin_pool.register_plugin(Bootstrap3TabCMSPlugin)
plugin_pool.register_plugin(Bootstrap3TabItemCMSPlugin)
plugin_pool.register_plugin(Bootstrap3AccordionCMSPlugin)
plugin_pool.register_plugin(Bootstrap3AccordionItemCMSPlugin)
plugin_pool.register_plugin(Bootstrap3CarouselCMSPlugin)
plugin_pool.register_plugin(Bootstrap3CarouselSlideCMSPlugin)
# plugin_pool.register_plugin(Bootstrap3CarouselSlideFolderCMSPlugin)
plugin_pool.register_plugin(Bootstrap3SpacerCMSPlugin)
plugin_pool.register_plugin(Bootstrap3FileCMSPlugin)
