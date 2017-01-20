# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django.core.exceptions
import django.forms
import django.forms.models
import django.template
import django.template.loader

from django.forms.widgets import Media, TextInput, Textarea
from django.utils.translation import ugettext_lazy as _

import cms.forms.fields
import cms.models

from djangocms_attributes_field.widgets import AttributesWidget

from . import models, constants


class RowPluginBaseForm(django.forms.models.ModelForm):
    create = django.forms.IntegerField(
        label=_('Create columns'),
        help_text=_('Number of columns to create in this row.'),
        required=False,
        min_value=0,
    )

    class Meta:
        model = models.Bootstrap3RowPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


extra_fields_row = {}
for size, name in constants.DEVICE_CHOICES:
    extra_fields_row['create_{}_col'.format(size)] = django.forms.IntegerField(
        label='col-{}-'.format(size),
        help_text=_('Width of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=1,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row['create_{}_offset'.format(size)] = django.forms.IntegerField(
        label='offset-'.format(size),
        help_text=_('Offset of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row['create_{}_push'.format(size)] = django.forms.IntegerField(
        label='push-'.format(size),
        help_text=_('Push of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row['create_{}_pull'.format(size)] = django.forms.IntegerField(
        label='pull-'.format(size),
        help_text=_('Pull of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )

RowPluginForm = type(
    str('RowPluginBaseForm'),
    (RowPluginBaseForm,),
    extra_fields_row
)


class ColumnPluginBaseForm(django.forms.models.ModelForm):
    create = django.forms.IntegerField(
        label=_('Adjust columns'),
        help_text=_('Adjust this column.'),
        required=False,
        min_value=0,
    )

    class Meta:
        model = models.Bootstrap3ColumnPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


extra_fields_column = {}
for size, name in constants.DEVICE_CHOICES:
    extra_fields_column['{}_col'.format(size)] = django.forms.IntegerField(
        label='col-{}-'.format(size),
        help_text=_('Width of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=1,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column['{}_offset'.format(size)] = django.forms.IntegerField(
        label='offset-'.format(size),
        help_text=_('Offset of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column['{}_push'.format(size)] = django.forms.IntegerField(
        label='push-'.format(size),
        help_text=_('Push of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column['{}_pull'.format(size)] = django.forms.IntegerField(
        label='pull-'.format(size),
        help_text=_('Pull of created columns '
                    '(can be edited later if required.)'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )

ColumnPluginForm = type(
    str('ColumnPluginBaseForm'),
    (ColumnPluginBaseForm,),
    extra_fields_column
)


class Bootstrap3CodePluginForm(django.forms.models.ModelForm):
    class Meta:
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'code': Textarea(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }


class LinkForm(django.forms.models.ModelForm):
    link_page = cms.forms.fields.PageSelectFormField(
        queryset=cms.models.Page.objects.drafts(),
        label=_('Internal link'),
        required=False,
    )

    def for_site(self, site):
        # override the page_link fields queryset to containt just pages for
        # current site
        self.fields['link_page'].queryset = cms.models.Page.objects.drafts().on_site(site)

    class Meta:
        model = models.Boostrap3ButtonPlugin
        exclude = (
            'page', 'position', 'placeholder', 'language', 'plugin_type',
        )
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'label': TextInput(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()

    def _get_media(self):
        """
        Provide a description of all media required to render the widgets on this form
        """
        media = Media()
        for field in self.fields.values():
            media = media + field.widget.media
        media._js = ['cms/js/libs/jquery.min.js'] + media._js
        return media
    media = property(_get_media)


class Boostrap3LabelPluginForm(django.forms.models.ModelForm):

    class Meta:
        model = models.Boostrap3LabelPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
        # When used inside djangocms-text-ckeditor
        # this causes the label field to be prefilled with the selected text.
        widgets = {
            'label': TextInput(attrs={'class': 'js-ckeditor-use-selected-text'}),
        }


class PanelPluginBaseForm(django.forms.models.ModelForm):
    create_heading = django.forms.BooleanField(
        label=_('Initial heading'),
        required=False,
        initial=False,
    )
    create_body = django.forms.BooleanField(
        label=_('Initial body'),
        required=False,
        initial=False,
    )
    create_footer = django.forms.BooleanField(
        label=_('Initial footer'),
        required=False,
        initial=False,
    )

    class Meta:
        model = models.Boostrap3PanelPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class CarouselPluginForm(django.forms.ModelForm):

    class Meta:
        fields = [
            'style',
            'transition_effect',
            'ride',
            'interval',
        ]
        model = models.Bootstrap3CarouselPlugin

    def clean_style(self):
        style = self.cleaned_data.get('style')
        template = 'aldryn_bootstrap3/plugins/carousel/{}/carousel.html'.format(
            style
        )
        # Check if template for style exists:
        try:
            django.template.loader.select_template([template])
        except django.template.TemplateDoesNotExist:
            raise django.forms.ValidationError(
                _('Not a valid style (template {path} does not exist)').format(path=template)
            )
        return style


class CarouselSlidePluginForm(django.forms.ModelForm):

    class Meta:
        fields = ['image', 'content', 'link_text', 'classes', 'link_attributes']
        model = models.Bootstrap3CarouselSlidePlugin

    def __init__(self, *args, **kwargs):
        super(CarouselSlidePluginForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget()
