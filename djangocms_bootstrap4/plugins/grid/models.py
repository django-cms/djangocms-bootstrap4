# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext, ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_attributes_field.fields import AttributesField


# The default grid size for Bootstrap 4 is 12. You can change this setting
# to whatever layout you require. We suggest that the value is at
# least devisable by 2, 3 and 4.
GRID_SIZE = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_SIZE',
    12,
)

# Bootstrap 4 provides 2 container types, .container and .container-fluid
# https://getbootstrap.com/docs/4.0/layout/grid/#no-gutters
GRID_CONTAINERS = getattr(
    settings,
    'DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS',
    (
        ('Fixed width', 'container'),
        ('Full width', 'container-fluid'),
    ),
)


@python_2_unicode_compatible
class Bootstrap4GridContainer(CMSPlugin):
    """
    Layout > Grid: "Container" Plugin
    https://getbootstrap.com/docs/4.0/layout/grid/
    """
    container_type = models.CharField(
        verbose_name=_('Container type'),
        choices=GRID_CONTAINERS,
        default=GRID_CONTAINERS[0][0],
        max_length=255,
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
    )

    def __str__(self):
        return str(self.container_type)


class Bootstrap4GridRow:
    pass


class Bootstrap4GridColumn:
    pass
