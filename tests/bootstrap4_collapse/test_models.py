from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_collapse.models import (
    Bootstrap5Collapse, Bootstrap5CollapseContainer, Bootstrap5CollapseTrigger,
)


class B5CollapseModelTestCase(TestCase):

    def test_collapse_instance(self):
        instance = Bootstrap5Collapse.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(collapse-1)")

    def test_collapse_trigger_instance(self):
        instance = Bootstrap5CollapseTrigger.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "()")

    def test_collapse_container_instance(self):
        instance = Bootstrap5CollapseContainer.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "()")
