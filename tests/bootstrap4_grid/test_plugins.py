# -*- coding: utf-8 -*-
import warnings

from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_grid.cms_plugins import (
    Bootstrap4GridColumnPlugin, Bootstrap4GridContainerPlugin,
    Bootstrap4GridRowPlugin,
)

from ..fixtures import B4TestFixture


class B4CarouselPluginTestCase(B4TestFixture, CMSTestCase):

    def test_container_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridContainerPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.assertEqual(
            plugin.plugin_type,
            "Bootstrap4GridContainerPlugin",
        )

    def test_grid_row_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridRowPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.assertEqual(
            plugin.plugin_type,
            "Bootstrap4GridRowPlugin",
        )

    def test_grid_column_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridColumnPlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.assertEqual(
            plugin.plugin_type,
            "Bootstrap4GridColumnPlugin",
        )

    def test_plugin_structure(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        container = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridContainerPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)
        self.assertEqual(response.status_code, 200)

        row = add_plugin(
            target=container,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridRowPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)
        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)
        self.assertEqual(response.status_code, 200)

        # add row with values
        add_plugin(
            target=row,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridColumnPlugin.__name__,
            language=self.language,
            xs_col=12,
        )
        self.page.publish(self.language)
        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)
        self.assertEqual(response.status_code, 200)

        # add row without values
        add_plugin(
            target=row,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridColumnPlugin.__name__,
            language=self.language,
        )
        self.page.publish(self.language)
        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)
        self.assertEqual(response.status_code, 200)

    def test_row_plugin_creation(self):
        request_url = self.get_add_plugin_uri(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4GridRowPlugin.__name__,
            language=self.language,
        )
        # create 5 column plugins
        data = {
            "create": 5,
            "tag_type": "div"
        }

        with self.login_user_context(self.superuser), warnings.catch_warnings():
            # hide the "DontUsePageAttributeWarning" warning when using
            # `get_add_plugin_uri` to get cleaner test results
            warnings.simplefilter("ignore")
            response = self.client.post(request_url, data)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<div class="success">')
