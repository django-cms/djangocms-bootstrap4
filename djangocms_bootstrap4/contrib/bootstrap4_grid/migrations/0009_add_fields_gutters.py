from django.db import migrations
import djangocms_bootstrap4.contrib.bootstrap4_grid.models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0008_rename_spacing_to_spacing_vertical'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='gutters_horizontal',
            field=enumfields.fields.EnumField(default='normal', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.models.GuttersHorizontal, max_length=32),
        ),
        migrations.AddField(
            model_name='bootstrap4gridrow',
            name='gutters_vertical',
            field=enumfields.fields.EnumField(default='none', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.models.GuttersVertical, max_length=32),
        ),
    ]
