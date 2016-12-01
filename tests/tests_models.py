# -*- coding: utf-8 -*-
from django.test import TestCase

from aldryn_bootstrap3.models import Boostrap3ButtonPlugin


class Boostrap3ButtonPluginTestCase(TestCase):

    def setUp(self):
        Boostrap3ButtonPlugin.objects.create(
            label='test',
        )

    def test_bootstrap3_button_instance(self):
        """Button instance has been created"""
        button = Boostrap3ButtonPlugin.objects.get(label='test')
        self.assertEqual(button.label, 'test')
