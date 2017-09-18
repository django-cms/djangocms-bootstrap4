# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django.forms.widgets

from . import constants
from .conf import settings


class ContextRenderer(django.forms.widgets.RadioFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/context.html',
            {'selects': self},
        )
        return rendered


class Context(django.forms.widgets.RadioSelect):
    renderer = ContextRenderer


class SizeRenderer(django.forms.widgets.RadioFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/size.html',
            {'selects': self},
        )
        return rendered


class Size(django.forms.widgets.RadioSelect):
    renderer = SizeRenderer


class Icon(django.forms.widgets.TextInput):
    def render(self, name, value, attrs=None, **kwargs):
        input_html = super(Icon, self).render(name, value, attrs=attrs, **kwargs)
        if value is None:
            value = ''
        iconset = value.split('-')[0] if value and '-' in value else ''
        iconset_prefexes = [s[1] for s in settings.ALDRYN_BOOTSTRAP3_ICONSETS]
        if len(settings.ALDRYN_BOOTSTRAP3_ICONSETS) and iconset not in iconset_prefexes:
            # invalid iconset! maybe because the iconset was removed from
            # the project. set it to the first in the list.
            iconset = settings.ALDRYN_BOOTSTRAP3_ICONSETS[0][1]
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/icon.html',
            {
                'input_html': input_html,
                'value': value,
                'name': name,
                'iconset': iconset,
                'is_required': self.is_required,
                'iconsets': settings.ALDRYN_BOOTSTRAP3_ICONSETS,
            },
        )
        return rendered


class MiniTextarea(django.forms.widgets.Textarea):
    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['cols'] = '120'
        attrs['rows'] = '1'
        super(MiniTextarea, self).__init__(attrs)


class LinkOrButtonRenderer(django.forms.widgets.RadioFieldRenderer):
    def render(self):
        from django.template.loader import render_to_string
        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/link_or_button.html',
            {'selects': self},
        )
        return rendered


class LinkOrButton(django.forms.widgets.RadioSelect):
    renderer = LinkOrButtonRenderer


class Responsive(django.forms.widgets.Textarea):
    def render(self, name, value, attrs=None):
        from django.template.loader import render_to_string
        widget_html = super(Responsive, self).render(name=name, value=value, attrs=attrs)

        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/responsive.html',
            {
                'widget_html': widget_html,
                'widget': self,
                'value': value,
                'name': name,
                'id': attrs.get('id', None),
                'attrs': attrs,
            },
        )
        return rendered


class ResponsivePrint(django.forms.widgets.Textarea):
    def render(self, name, value, attrs=None):
        from django.template.loader import render_to_string
        widget_html = super(ResponsivePrint, self).render(
            name=name, value=value, attrs=attrs)

        rendered = render_to_string(
            'admin/aldryn_bootstrap3/widgets/responsive_print.html',
            {
                'widget_html': widget_html,
                'widget': self,
                'value': value,
                'name': name,
                'id': attrs.get('id', None),
                'attrs': attrs,
            },
        )
        return rendered
