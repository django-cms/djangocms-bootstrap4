from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_listgroup.models import (
    Bootstrap4ListGroup, Bootstrap4ListGroupItem,
)


class B4ListGroupModelTestCase(TestCase):

    def test_list_group_instance(self):
        instance = Bootstrap4ListGroup.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
        instance.list_group_flush = True
        self.assertEqual(instance.get_short_description(), ".list-group-flush")

    def test_list_group_item_instance(self):
        instance = Bootstrap4ListGroupItem.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
        instance.list_context = "primary"
        self.assertEqual(instance.get_short_description(), ".list-group-item-primary")
        instance.list_state = "active"
        self.assertEqual(instance.get_short_description(), ".list-group-item-primary .active")
