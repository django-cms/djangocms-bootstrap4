from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_tabs.models import (
    Bootstrap5Tab, Bootstrap5TabItem,
)


class B5TabsModelTestCase(TestCase):

    def test_tab_instance(self):
        instance = Bootstrap5Tab.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(nav-tabs)")
        instance.tab_alignment = "nav-fill"
        self.assertEqual(instance.get_short_description(), "(nav-tabs) .nav-fill")

    def test_tab_item_instance(self):
        instance = Bootstrap5TabItem.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
