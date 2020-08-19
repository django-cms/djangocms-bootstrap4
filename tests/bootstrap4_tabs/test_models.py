from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_tabs.models import (
    Bootstrap4Tab, Bootstrap4TabItem,
)


class B4TabsModelTestCase(TestCase):

    def test_tab_instance(self):
        instance = Bootstrap4Tab.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(nav-tabs)")
        instance.tab_alignment = "nav-fill"
        self.assertEqual(instance.get_short_description(), "(nav-tabs) .nav-fill")

    def test_tab_item_instance(self):
        instance = Bootstrap4TabItem.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
