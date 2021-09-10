from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_bootstrap5.contrib.bootstrap5_collapse.cms_plugins import (
    Bootstrap5CollapseContainerPlugin, Bootstrap5CollapsePlugin,
    Bootstrap5CollapseTriggerPlugin,
)

from ..fixtures import B5TestFixture


class B5CollapsePluginTestCase(B5TestFixture, CMSTestCase):

    def test_collapse_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CollapsePlugin.__name__,
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
            plugin_type=Bootstrap5CollapseTriggerPlugin.__name__,
            language=self.language,
            identifier=10,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'aria-controls="container-10"')
        self.assertContains(response, 'data-bs-target="#container-10"')
        self.assertContains(response, 'id="trigger-10"')

    def test_collapse_container_plugin(self):
        parent = add_plugin(
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CollapsePlugin.__name__,
            language=self.language,
        )
        plugin = add_plugin(
            target=parent,
            placeholder=self.placeholder,
            plugin_type=Bootstrap5CollapseContainerPlugin.__name__,
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
