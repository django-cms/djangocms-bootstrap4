# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import TagTypeField, AttributesField

# TODO leaving this comment for now
# data-toggle="collapse" data-target="#collapseExample"
# aria-expanded="false" aria-controls="collapseExample">
# data-target can also be classes
# data-parent links to the wrapper collapse
# <div class="collapse" id="collapseExample">


@python_2_unicode_compatible
class Bootstrap4Collapse(CMSPlugin):
    """
    Component > "Collapse" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    siblings = models.CharField(
        verbose_name=_('Siblings'),
        default='.card',
        max_length=255,
        help_text=_('Element to be used to create accordions.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField(
        excluded_keys=['id']
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '(collapse-{})'.format(str(self.pk))


@python_2_unicode_compatible
class Bootstrap4CollapseTrigger(CMSPlugin):
    """
    Component > "Collapse Trigger" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    identifier = models.SlugField(
        verbose_name=_('Unique identifier'),
        max_length=255,
        blank=False,
        help_text=_('Identifier to connect trigger with container.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField(
        excluded_keys=[
            'data-toggle', 'data-target', 'data-parent',
            'aria-expanded', 'aria-controls', 'role',
        ]
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.identifier)


@python_2_unicode_compatible
class Bootstrap4CollapseContainer(CMSPlugin):
    """
    Component > "Collapse Container" Plugin
    https://getbootstrap.com/docs/4.0/components/collapse/
    """
    identifier = models.SlugField(
        verbose_name=_('Unique identifier'),
        max_length=255,
        blank=False,
        help_text=_('Identifier to connect trigger with container.'),
    )
    tag_type = TagTypeField()
    attributes = AttributesField(
        excluded_keys=[
            'data-toggle', 'data-target', 'data-parent',
            'aria-expanded', 'aria-controls', 'role',
        ]
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.identifier)
