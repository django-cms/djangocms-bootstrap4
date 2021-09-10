from django.test import TestCase

from djangocms_bootstrap5.contrib.bootstrap5_badge.models import (
    Bootstrap5Badge,
)


class B5BadgeModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap5Badge.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(primary)")
