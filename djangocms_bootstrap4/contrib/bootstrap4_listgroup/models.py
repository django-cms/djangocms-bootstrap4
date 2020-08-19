from django.db import models
from django.utils.translation import gettext_lazy as _

from cms.models import CMSPlugin

from djangocms_bootstrap4.constants import COLOR_STYLE_CHOICES
from djangocms_bootstrap4.fields import AttributesField, TagTypeField

from .constants import LISTGROUP_STATE_CHOICES


class Bootstrap4ListGroup(CMSPlugin):
    """
    Components > "List Group" Plugin
    https://getbootstrap.com/docs/4.0/components/list-group/
    """
    list_group_flush = models.BooleanField(
        verbose_name=_('List group flush'),
        default=False,
        help_text=_('Create lists of content in a card with a flush list group.')
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = ''
        if self.list_group_flush:
            text += '.list-group-flush'
        return text


class Bootstrap4ListGroupItem(CMSPlugin):
    """
    Components > "List Group Ite" Plugin
    https://getbootstrap.com/docs/4.0/components/list-group/
    """
    list_context = models.CharField(
        verbose_name=_('Context'),
        choices=COLOR_STYLE_CHOICES,
        blank=True,
        max_length=255,
    )
    list_state = models.CharField(
        verbose_name=_('State'),
        choices=LISTGROUP_STATE_CHOICES,
        blank=True,
        max_length=255,
    )
    tag_type = TagTypeField()
    attributes = AttributesField()

    def __str__(self):
        return str(self.pk)

    def get_short_description(self):
        text = []
        if self.list_context:
            text.append('.list-group-item-{}'.format(self.list_context))
        if self.list_state:
            text.append('.{}'.format(self.list_state))
        return ' '.join(text)
