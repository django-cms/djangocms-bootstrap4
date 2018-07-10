# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_bootstrap4.fields


def migrate_column_size(apps, schema_editor):
    Column = apps.get_model('bootstrap4_grid', 'Bootstrap4GridColumn')
    plugins = Column.objects.all()

    for plugin in plugins:
        if not plugin.xs_col and plugin.column_size:
            plugin.xs_col = plugin.column_size
            plugin.save()

def migrate_column_size_back(apps, schema_editor):
    Column = apps.get_model('bootstrap4_grid', 'Bootstrap4GridColumn')
    plugins = Column.objects.all()

    for plugin in plugins:
        if plugin.xs_col:
            plugin.column_size = plugin.xs_col
            plugin.save()


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0002_auto_20180709_0808'),
    ]

    operations = [
        migrations.RunPython(migrate_column_size, migrate_column_size_back)
    ]
