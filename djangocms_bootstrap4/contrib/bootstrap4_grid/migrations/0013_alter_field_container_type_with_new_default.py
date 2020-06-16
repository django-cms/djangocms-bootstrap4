from django.db import migrations
import djangocms_bootstrap4.contrib.bootstrap4_grid.models
import djangocms_bootstrap4.contrib.bootstrap4_grid.constants
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0012_add_field_width_internal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4gridcontainer',
            name='container_type',
            field=enumfields.fields.EnumField(default='container-fluid', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerType, max_length=255, verbose_name='External width'),
        ),
    ]
