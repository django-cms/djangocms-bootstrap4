# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from aldryn_client import forms


class Form(forms.BaseForm):
    enable_glyphicons = forms.CheckboxField(
        'Enable Glyphicons',
        required=False,
        initial=True,
        help_text='If you disable this, remember to also update your sass config to not load the font.',
    )
    enable_fontawesome = forms.CheckboxField(
        'Enable Fontawesome',
        required=False,
        initial=True,
        help_text='If you disable this, remember to also update your sass config to not load the font.',
    )

    def to_settings(self, data, settings):
        choices = []
        if data['enable_glyphicons']:
            choices.append(
                ('glyphicons', 'glyphicons', 'Glyphicons')
            )
        if data['enable_fontawesome']:
            choices.append(
                ('fontawesome', 'fa', 'Fontawesome')
            )
        settings['ALDRYN_BOOTSTRAP3_ICONSETS'] = choices
        return settings
