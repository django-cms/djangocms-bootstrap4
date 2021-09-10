from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_content.models import (
    Bootstrap5Blockquote, Bootstrap5Code, Bootstrap5Figure,
)


class B5ContentModelTestCase(TestCase):

    def test_code_instance(self):
        instance = Bootstrap5Code.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "<code>")

    def test_blockquote_instance(self):
        instance = Bootstrap5Blockquote.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")

    def test_figure_instance(self):
        instance = Bootstrap5Figure.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
