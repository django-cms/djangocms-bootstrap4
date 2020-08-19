from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_badge.models import (
    Bootstrap4Badge,
)


class B4BadgeModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Badge.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(primary)")
