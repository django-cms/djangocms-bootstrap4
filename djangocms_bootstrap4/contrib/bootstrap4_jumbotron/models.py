# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField


@python_2_unicode_compatible
class Bootstrap4Jumbotron(CMSPlugin):
    """
    Components > "Jumbotron" Plugin
    https://getbootstrap.com/docs/4.0/components/jumbotron/
    """
    fluid = models.BooleanField(
        verbose_name=_('Fluid'),
        default=False,
        help_text=_('Adds the .jumbotron-fluid class.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        if self.fluid:
            text = '({})'.format(_('Fluid'))
        return text
