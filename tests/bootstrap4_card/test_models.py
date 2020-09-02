from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_card.models import (
    Bootstrap4Card, Bootstrap4CardInner,
)


class B4CardModelTestCase(TestCase):

    def test_card_instance(self):
        instance = Bootstrap4Card.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(card)")
        instance.card_context = "primary"
        self.assertEqual(instance.get_short_description(), "(card) .bg-primary")
        instance.card_outline = True
        self.assertEqual(instance.get_short_description(), "(card) .border-primary")
        instance.card_alignment = "center"
        self.assertEqual(instance.get_short_description(), "(card) .border-primary .center")

    def test_card_inner_instance(self):
        instance = Bootstrap4CardInner.objects.create()
        self.assertEqual(str(instance), "1")
        self.assertEqual(instance.get_short_description(), "(card-body)")
