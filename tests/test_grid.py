# -*- coding: utf-8 -*-
from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.constants import TAG_CHOICES
from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import (
    GRID_CONTAINER_CHOICES,
)


class ContainerPluginTestCase(CMSTestCase):

    def setUp(self):
        self.language = 'en'
        self.page = create_page(
            title='content',
            template='page.html',
            language=self.language,
        )
        self.placeholder = self.page.placeholders.get(slot='content')
        self.superuser = self.get_superuser()

    def tearDown(self):
        self.page.delete()

    def test_add_container_plugin(self):
        plugins = self.placeholder.get_plugins(self.language)
        endpoint = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type='Bootstrap4GridContainerPlugin',
            language=self.language,
        )

        with self.login_user_context(self.superuser):
            data = {
                'container_type': GRID_CONTAINER_CHOICES[0][0],
                'tag_type': TAG_CHOICES[0][0],
            }
            response = self.client.post(endpoint, data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(plugins.count(), 1)

    def test_add_row_plugin(self):
        plugins = self.placeholder.get_plugins(self.language)
        endpoint = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type='Bootstrap4GridRowPlugin',
            language=self.language,
        )

        with self.login_user_context(self.superuser):
            data = {
                'tag_type': TAG_CHOICES[0][0],
            }
            response = self.client.post(endpoint, data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(plugins.count(), 1)

    def test_add_column_plugin(self):
        plugins = self.placeholder.get_plugins(self.language)
        endpoint = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type='Bootstrap4GridColumnPlugin',
            language=self.language,
        )

        with self.login_user_context(self.superuser):
            data = {
                'tag_type': TAG_CHOICES[0][0],
            }
            response = self.client.post(endpoint, data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(plugins.count(), 1)

    def test_row_plugins(self):
        row = add_plugin(
            self.placeholder,
            "Bootstrap4GridRowPlugin",
            self.language,
        )
        self.assertEqual(row.get_short_description(), '(0 columns)')

    def test_column_size_plugin(self):
        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
            xs_col=2,
            sm_col=4,
            md_col=6,
            lg_col=8,
            xl_col=10,
        )
        self.assertEqual(
            column.get_grid_values(),
            ['col-2', 'col-sm-4', 'col-md-6', 'col-lg-8', 'col-xl-10'],
        )

        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
        )
        self.assertEqual(column.get_grid_values(), [])

    def test_column_order_plugin(self):
        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
            xs_order=2,
            sm_order=4,
            md_order=6,
            lg_order=8,
            xl_order=10,
        )
        self.assertEqual(
            column.get_grid_values(),
            ['order-2', 'order-sm-4', 'order-md-6', 'order-lg-8', 'order-xl-10'],
        )

        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
            xs_order=0,
            sm_order=0,
            md_order=0,
            lg_order=0,
            xl_order=0,
        )
        self.assertEqual(
            column.get_grid_values(),
            ['order-0', 'order-sm-0', 'order-md-0', 'order-lg-0', 'order-xl-0'],
        )

    def test_column_offset_plugin(self):
        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
            xs_offset=2,
            sm_offset=4,
            md_offset=6,
            lg_offset=8,
            xl_offset=10,
        )
        self.assertEqual(
            column.get_grid_values(),
            ['offset-2', 'offset-sm-4', 'offset-md-6', 'offset-lg-8', 'offset-xl-10'],
        )

        column = add_plugin(
            self.placeholder,
            "Bootstrap4GridColumnPlugin",
            self.language,
            xs_offset=0,
            sm_offset=0,
            md_offset=0,
            lg_offset=0,
            xl_offset=0,
        )
        self.assertEqual(
            column.get_grid_values(),
            ['offset-0', 'offset-sm-0', 'offset-md-0', 'offset-lg-0', 'offset-xl-0'],
        )
