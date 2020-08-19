from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.fields import AttributesField, TagTypeField


# TODO leaving this comment for now
# data-toggle="collapse" data-target="#collapseExample"
# aria-expanded="false" aria-controls="collapseExample">
# data-target can also be classes
# data-parent links to the wrapper collapse
# <div class="collapse" id="collapseExample">


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
