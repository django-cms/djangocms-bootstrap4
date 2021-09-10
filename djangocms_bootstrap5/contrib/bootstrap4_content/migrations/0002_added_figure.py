from django.db import migrations, models

import djangocms_bootstrap5.fields
from djangocms_bootstrap5.constants import ALIGN_CHOICES


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('bootstrap5_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bootstrap5Figure',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(related_name='bootstrap5_content_bootstrap5figure', primary_key=True, parent_link=True, auto_created=True, to='cms.CMSPlugin', serialize=False, on_delete=models.CASCADE)),
                ('figure_caption', models.CharField(verbose_name='Caption', max_length=255)),
                ('figure_alignment', models.CharField(verbose_name='Alignment', default=ALIGN_CHOICES[0][0], choices=ALIGN_CHOICES, blank=True, max_length=255)),
                ('attributes', djangocms_bootstrap5.fields.AttributesField(verbose_name='Attributes', default=dict, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
