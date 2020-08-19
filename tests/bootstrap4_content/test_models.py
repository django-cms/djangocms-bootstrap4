from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_content.models import (
    Bootstrap4Blockquote, Bootstrap4Code, Bootstrap4Figure,
)


class B4ContentModelTestCase(TestCase):

    def test_code_instance(self):
        instance = Bootstrap4Code.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "<code>")

    def test_blockquote_instance(self):
        instance = Bootstrap4Blockquote.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")

    def test_figure_instance(self):
        instance = Bootstrap4Figure.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
