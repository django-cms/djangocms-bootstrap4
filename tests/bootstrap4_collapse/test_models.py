from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_collapse.models import (
    Bootstrap4Collapse, Bootstrap4CollapseContainer, Bootstrap4CollapseTrigger,
)


class B4CollapseModelTestCase(TestCase):

    def test_collapse_instance(self):
        instance = Bootstrap4Collapse.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(collapse-1)")

    def test_collapse_trigger_instance(self):
        instance = Bootstrap4CollapseTrigger.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "()")

    def test_collapse_container_instance(self):
        instance = Bootstrap4CollapseContainer.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "()")
