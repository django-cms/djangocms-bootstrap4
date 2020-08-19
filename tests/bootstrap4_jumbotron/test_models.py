from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_jumbotron.models import (
    Bootstrap4Jumbotron,
)


class B4JumbotronModelTestCase(TestCase):

    def test_instance(self):
        instance = Bootstrap4Jumbotron.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "")
        instance.fluid = True
        self.assertEqual(instance.get_short_description(), "(Fluid)")
