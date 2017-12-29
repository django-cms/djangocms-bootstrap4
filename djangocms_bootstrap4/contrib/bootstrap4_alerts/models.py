# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField
from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES


@python_2_unicode_compatible
class Bootstrap4Alerts(CMSPlugin):
    """
    Components > "Alerts" Plugin
    https://getbootstrap.com/docs/4.0/components/alerts/
    """
    alert_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        default=COLOR_STYLE_CHOICES[0][0],
        max_length=255,
    )
    alert_dismissable = models.BooleanField(
        verbose_name=_('Dismissable'),
        default=False,
        help_text=_('Allows the alert to be closed.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.alert_context)
