# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from djangocms_link.forms import LinkForm
from djangocms_bootstrap4.constants import DEVICE_SIZES

from .models import Bootstrap4Link


class HorizontalRadioRenderer(forms.RadioSelect.renderer):

    def render(self):
        return mark_safe('\n'.join(['%s\n' % w for w in self]))


class Bootstrap4LinkForm(LinkForm, models.ModelForm):

    class Meta:
        model = Bootstrap4Link
        widgets = {
            'link_type': forms.RadioSelect(
                renderer=HorizontalRadioRenderer
            ),
        }
        fields = '__all__'
