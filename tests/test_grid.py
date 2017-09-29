# -*- coding: utf-8 -*-
from django.test import TestCase

from cms.api import add_plugin, create_page

from djangocms_helper.base_test import BaseTestCase

from djangocms_bootstrap4.contrib.bootstrap4_grid.models import (
    Bootstrap4GridContainer,
    Bootstrap4GridRow,
    Bootstrap4GridColumn,
)
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import (
    GRID_CONTAINERS,
    GRID_ROW_VERTICAL_ALIGNMENT,
    GRID_SIZE,
)


class GridInstanceTestCase(TestCase):

    def setUp(self):
        Bootstrap4GridContainer.objects.create(
            container_type=GRID_CONTAINERS[0][0],
        )
        Bootstrap4GridRow.objects.create(pk=0)
        Bootstrap4GridColumn.objects.create(pk=0)

    def test_container_instance(self):
        container = Bootstrap4GridContainer.objects.get(
            container_type=GRID_CONTAINERS[0][0]
        )
        self.assertEqual(container.container_type, GRID_CONTAINERS[0][0])

    def test_row_instance(self):
        container = Bootstrap4GridRow.objects.get(
            pk=0,
        )
        self.assertEqual(container.pk, 0)

    def test_column_instance(self):
        container = Bootstrap4GridColumn.objects.get(
            pk=0,
        )
        self.assertEqual(container.pk, 0)


class ContainerPluginTestCase(BaseTestCase):

    def setUp(self):
        self.page = create_page(
            title='content',
            template='page.html',
            language='en',
        )

    def test_container_plugin(self):
        plugin = add_plugin(
            self.page.placeholders.get(slot='content'),
            'Bootstrap4GridContainerPlugin',
            'en',
            container_type=GRID_CONTAINERS[0][0],
        )
        self.assertEqual(
            plugin.container_type,
            GRID_CONTAINERS[0][0],
        )

    def test_row_plugin(self):
        plugin = add_plugin(
            self.page.placeholders.get(slot='content'),
            'Bootstrap4GridRowPlugin',
            'en',
            vertical_alignment=GRID_ROW_VERTICAL_ALIGNMENT[0][0],
        )
        self.assertEqual(
            plugin.vertical_alignment,
            GRID_ROW_VERTICAL_ALIGNMENT[0][0],
        )

    def test_column_plugin(self):
        plugin = add_plugin(
            self.page.placeholders.get(slot='content'),
            'Bootstrap4GridColumnPlugin',
            'en',
            column_size=GRID_SIZE,
        )
        self.assertEqual(
            plugin.column_size,
            GRID_SIZE,
        )
