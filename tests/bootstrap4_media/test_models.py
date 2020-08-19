from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_media.models import (
    Bootstrap4Media, Bootstrap4MediaBody,
)


class B4MediaModelTestCase(TestCase):

    def test_media_instance(self):
        instance = Bootstrap4Media.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")

    def test_media_body_instance(self):
        instance = Bootstrap4MediaBody.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
