from django.db import migrations, models

import djangocms_bootstrap5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap5_grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap5gridcolumn',
            name='lg_offset',
            field=djangocms_bootstrap5.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap5gridcolumn',
            name='md_offset',
            field=djangocms_bootstrap5.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap5gridcolumn',
            name='sm_offset',
            field=djangocms_bootstrap5.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap5gridcolumn',
            name='xl_offset',
            field=djangocms_bootstrap5.fields.IntegerRangeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bootstrap5gridcolumn',
            name='xs_offset',
            field=djangocms_bootstrap5.fields.IntegerRangeField(blank=True, null=True),
        ),
    ]
