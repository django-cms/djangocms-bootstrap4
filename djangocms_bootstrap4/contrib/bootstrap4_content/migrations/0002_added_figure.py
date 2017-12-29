# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_bootstrap4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('bootstrap4_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap4Figure',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='bootstrap4_content_bootstrap4figure', primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin', serialize=False)),
                ('figure_caption', models.CharField(verbose_name='Caption', max_length=255)),
                ('figure_alignment', models.CharField(verbose_name='Alignment', default='', choices=[('', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')], blank=True, max_length=255)),
                ('attributes', djangocms_bootstrap4.fields.AttributesField(verbose_name='Attributes', default=dict, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='bootstrap4code',
            name='tag_type',
            field=models.CharField(verbose_name='Code type', default='', choices=[('', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')], max_length=255),
        ),
    ]
