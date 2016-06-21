# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import django.core.exceptions
import django.forms
import django.forms.models
import django.template
import django.template.loader

from django.forms.widgets import Media
from django.utils.translation import ugettext_lazy as _

import cms.forms.fields
import cms.models

from djangocms_attributes_field.widgets import AttributesWidget

from . import models, constants


class RowPluginBaseForm(django.forms.models.ModelForm):
    create = django.forms.IntegerField(
        label=_('Create Columns'),
        help_text=_('Create this number of columns inside'),
        required=False,
        min_value=0,
    )

    class Meta:
        model = models.Bootstrap3RowPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


class ColumnPluginBaseForm(django.forms.models.ModelForm):
    create = django.forms.IntegerField(
        label=_('Adapt Columns'),
        help_text=_('Adapt this column'),
        required=False,
        min_value=0,
    )

    class Meta:
        model = models.Bootstrap3ColumnPlugin
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


extra_fields_row = {}
for size, name in constants.DEVICE_CHOICES:
    extra_fields_row["create_{}_col".format(size)] = django.forms.IntegerField(
        label=_('col-{}-'.format(size)),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=1,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row["create_{}_offset".format(size)] = django.forms.IntegerField(
        label=_('offset-'.format(size)),
        help_text=('Offset of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row["create_{}_push".format(size)] = django.forms.IntegerField(
        label=_('push-'.format(size)),
        help_text=('Push of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_row["create_{}_pull".format(size)] = django.forms.IntegerField(
        label=_('pull-'.format(size)),
        help_text=('Pull of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )

extra_fields_column = {}
for size, name in constants.DEVICE_CHOICES:
    extra_fields_column["{}_col".format(size)] = django.forms.IntegerField(
        label=_('col-{}-'.format(size)),
        help_text=('Width of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=1,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column["{}_offset".format(size)] = django.forms.IntegerField(
        label=_('offset-'.format(size)),
        help_text=('Offset of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column["{}_push".format(size)] = django.forms.IntegerField(
        label=_('push-'.format(size)),
        help_text=('Push of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )
    extra_fields_column["{}_pull".format(size)] = django.forms.IntegerField(
        label=_('pull-'.format(size)),
        help_text=('Pull of created columns. You can still change the width of the column afterwards.'),
        required=False,
        min_value=0,
        max_value=constants.GRID_SIZE,
    )

RowPluginForm = type(str('RowPluginBaseForm'), (RowPluginBaseForm,), extra_fields_row)
ColumnPluginForm = type(str('ColumnPluginBaseForm'), (ColumnPluginBaseForm,), extra_fields_column)


class LinkForm(django.forms.models.ModelForm):
    link_page = cms.forms.fields.PageSelectFormField(
        queryset=cms.models.Page.objects.drafts(),
        label=_("Page"),
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

    def __init__(self, *args, **kwargs):
        super(LinkForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget(val_attrs={'style': 'width:500px!important'})

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

    def clean(self):
        cleaned_data = super(LinkForm, self).clean()
        link_fields = {
            'link_url': cleaned_data.get("link_url"),
            'link_page': cleaned_data.get("link_page"),
            'link_file': cleaned_data.get("link_file"),
            'link_mailto': cleaned_data.get("link_mailto"),
            'link_phone': cleaned_data.get("link_phone"),
        }
        error_msg = _("Only one of Page, File, Link, Email address or Phone is allowed.")
        if len([i for i in link_fields.values() if i]) > 1:
            for field, value in link_fields.items():
                if value:
                    self._errors[field] = self.error_class([error_msg])
            raise django.core.exceptions.ValidationError(error_msg)
        return cleaned_data


class PanelPluginBaseForm(django.forms.models.ModelForm):
    create_heading = django.forms.BooleanField(required=False, initial=False)
    create_body = django.forms.BooleanField(required=False, initial=False)
    create_footer = django.forms.BooleanField(required=False, initial=False)

    class Meta:
        model = models.Boostrap3PanelPlugin
        # fields = ('classes',)
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
            style)
        # Check if template for style exists:
        try:
            django.template.loader.select_template([template])
        except django.template.TemplateDoesNotExist:
            raise django.forms.ValidationError(
                _("Not a valid style (Template %s does not exist)") % template
            )
        return style


class CarouselSlidePluginForm(django.forms.ModelForm):

    class Meta:
        fields = ['image', 'content', 'link_text', 'classes', 'link_attributes', ]
        model = models.Bootstrap3CarouselSlidePlugin

    def __init__(self, *args, **kwargs):
        super(CarouselSlidePluginForm, self).__init__(*args, **kwargs)
        self.fields['link_attributes'].widget = AttributesWidget(val_attrs={'style': 'width:500px!important'})

