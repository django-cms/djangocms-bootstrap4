from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_media.models import (
    Bootstrap5Media, Bootstrap5MediaBody,
)


class B5MediaModelTestCase(TestCase):

    def test_media_instance(self):
        instance = Bootstrap5Media.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")

    def test_media_body_instance(self):
        instance = Bootstrap5MediaBody.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
