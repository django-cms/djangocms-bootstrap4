from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap4.contrib.bootstrap4_collapse.cms_plugins import (
    Bootstrap4CollapseContainerPlugin, Bootstrap4CollapsePlugin,
    Bootstrap4CollapseTriggerPlugin,
)

from ..fixtures import B4TestFixture


class B4CollapsePluginTestCase(B4TestFixture, CMSTestCase):

    def test_collapse_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CollapsePlugin.__name__,
            language=self.language,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'data-children=".card"')
        self.assertContains(response, 'role="tablist"')

    def test_collapse_trigger_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CollapseTriggerPlugin.__name__,
            language=self.language,
            identifier=10,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'aria-controls="container-10"')
        self.assertContains(response, 'data-target="#container-10"')
        self.assertContains(response, 'id="trigger-10"')

    def test_collapse_container_plugin(self):
        parent = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CollapsePlugin.__name__,
            language=self.language,
        )
        plugin = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=Bootstrap4CollapseContainerPlugin.__name__,
            language=self.language,
            identifier=10,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'aria-labelledby="trigger-10"')
        self.assertContains(response, 'container-10')
