from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_alerts.models import (
    Bootstrap4Alerts,
)


class B4AlertModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Alerts.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(primary)")
