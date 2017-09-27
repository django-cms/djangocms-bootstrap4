# -*- coding: utf-8 -*-
from django.test import TestCase

from djangocms_bootstrap4.contrib.bootstrap4_grid.models import (
    GRID_CONTAINERS,
    Bootstrap4GridContainer,
)


class Bootstrap4GridContainerPlugin(TestCase):
    def setUp(self):
        Bootstrap4GridContainer.objects.create(
            container_type=GRID_CONTAINERS[0][0],
        )

    def test_container_instance(self):
        container = Bootstrap4GridContainer.objects.get(
            container_type=GRID_CONTAINERS[0][0]
        )
        self.assertEqual(container.container_type, GRID_CONTAINERS[0][0])
