from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap5.fields import AttributesField, TagTypeField


# TODO leaving this comment for now
# data-bs-toggle="collapse" data-bs-target="#collapseExample"
# aria-expanded="false" aria-controls="collapseExample">
# data-bs-target can also be classes
# data-bs-parent links to the wrapper collapse
# <div class="collapse" id="collapseExample">


class Bootstrap5Collapse(CMSPlugin):
    """
    Component > "Collapse" Plugin
    https://getbootstrap.com/docs/5.0/components/collapse/
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


class Bootstrap5CollapseTrigger(CMSPlugin):
    """
    Component > "Collapse Trigger" Plugin
    https://getbootstrap.com/docs/5.0/components/collapse/
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
            'data-bs-toggle', 'data-bs-target', 'data-bs-parent',
            'aria-expanded', 'aria-controls', 'role',
        ]
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.identifier)


class Bootstrap5CollapseContainer(CMSPlugin):
    """
    Component > "Collapse Container" Plugin
    https://getbootstrap.com/docs/5.0/components/collapse/
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
            'data-bs-toggle', 'data-bs-target', 'data-bs-parent',
            'aria-expanded', 'aria-controls', 'role',
        ]
    )

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        return '({})'.format(self.identifier)
