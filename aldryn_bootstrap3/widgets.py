# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import string
import itertools
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.html import format_html, format_html_join

from .conf import settings


class BreakpointsRenderer(widgets.CheckboxFieldRenderer):
    def render(self):
        return format_html('<div class="form-row">{0}</div>',
            format_html_join('', '<div class="field-box">'
                '<div class="container-thumbnail"><i style="font-size: 60px;" class="icon-{1}"></i><div class="label">{0}</div></div>'
                '</div>', ((force_text(w), settings.ALDRYN_BOOTSTRAP3_BREAKPOINTS[w.choice_value][1]) for w in self)
            ))


class Breakpoint(widgets.CheckboxSelectMultiple):
    renderer = BreakpointsRenderer
    # widgets.CheckboxSelectMultiple(choices=WIDGET_CHOICES, renderer=ContainerBreakpointsRenderer)
