# -*- coding: utf-8 -*-
from cms.plugin_pool import plugin_pool

from .plugins.grid.cms_plugins import Bootstrap4GridContainerPlugin


plugin_pool.register_plugin(Bootstrap4GridContainerPlugin)
