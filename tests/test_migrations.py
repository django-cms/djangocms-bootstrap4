# original from
# http://tech.octopus.energy/news/2016/01/21/testing-for-missing-migrations-in-django.html
from distutils.version import LooseVersion
from io import StringIO

from django.core.management import call_command
from django.test import TestCase, override_settings

from cms import __version__


class MigrationTestCase(TestCase):

    @override_settings(MIGRATION_MODULES={})
    def test_for_missing_migrations(self):
        if LooseVersion("3.9") <= LooseVersion(__version__) < LooseVersion("3.10"):
            # django-cms 3.9 creates migrations to BigAutoField hence skip this test
            return

        output = StringIO()
        options = {
            'interactive': False,
            'dry_run': True,
            'stdout': output,
            'check_changes': True,
        }

        try:
            call_command('makemigrations', **options)
        except SystemExit as e:
            status_code = str(e)
        else:
            # the "no changes" exit code is 0
            status_code = '0'

        if status_code == '1':
            self.fail(f'There are missing migrations:\n {output.getvalue()}')
