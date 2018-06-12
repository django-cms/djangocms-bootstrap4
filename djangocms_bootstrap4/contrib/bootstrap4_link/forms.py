# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from djangocms_link.forms import LinkForm

from .constants import LINK_CHOICES
from .models import Bootstrap4Link


class Bootstrap4LinkForm(LinkForm):
    link_type = forms.ChoiceField(
        choices=LINK_CHOICES,
        initial=LINK_CHOICES[0][0],
        widget=forms.RadioSelect(attrs={'class': 'inline-block'}),
    )

    class Meta:
        model = Bootstrap4Link
        fields = '__all__'
