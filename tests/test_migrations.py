# -*- coding: utf-8 -*-
# original from
# http://tech.octopus.energy/news/2016/01/21/testing-for-missing-migrations-in-django.html
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from django.core.management import call_command
from django.test import TestCase, override_settings
from django.utils.six import text_type


class MigrationTestCase(TestCase):

    @override_settings(MIGRATION_MODULES={})
    def test_for_missing_migrations(self):
        output = StringIO()
        try:
            call_command(
                'makemigrations',
                interactive=False,
                dry_run=True,
                exit_code=True,
                stdout=output,
            )
        except SystemExit as e:
            # The exit code will be 1 when there are no missing migrations
            assert(text_type(e) == '1')
        else:
            self.fail(
                'There are missing migrations:\n {}'.format(output.getvalue())
            )
