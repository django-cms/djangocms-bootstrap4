# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aldryn_bootstrap3', '0007_auto_20160705_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap3accordionitemplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3accordionplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslidefolderplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3carouselslideplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3columnplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupitemplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3listgroupplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='bootstrap3rowplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='+', primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
