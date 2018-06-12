# -*- coding: utf-8 -*-
from cms.api import create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_grid.constants import (
    GRID_CONTAINER_CHOICES,
)
from djangocms_bootstrap4.constants import TAG_CHOICES


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
