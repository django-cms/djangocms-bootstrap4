from django.db import migrations
import djangocms_bootstrap4.contrib.bootstrap4_grid.models
import djangocms_bootstrap4.contrib.bootstrap4_grid.constants
import enumfields.fields
from enumfields import Enum


class SpacingVerticalType(Enum):
    """
    for backward migration compatibility
    """
    MARGIN = 'margin'
    PADDING = 'padding'


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0006_add_fields_background_and_spacing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bootstrap4gridcontainer',
            name='spacing_vertical_type',
            field=enumfields.fields.EnumField(default='margin', enum=SpacingVerticalType, max_length=255, verbose_name='Vertical spacing type'),
        ),
        migrations.AlterField(
            model_name='bootstrap4gridcontainer',
            name='background',
            field=enumfields.fields.EnumField(default='background-none', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerBackground, max_length=255, verbose_name='Background'),
        ),
        migrations.AlterField(
            model_name='bootstrap4gridcontainer',
            name='container_type',
            field=enumfields.fields.EnumField(default='container', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerType, max_length=255, verbose_name='Container width'),
        ),
        migrations.AlterField(
            model_name='bootstrap4gridcontainer',
            name='spacing',
            field=enumfields.fields.EnumField(default='none', enum=djangocms_bootstrap4.contrib.bootstrap4_grid.constants.GridContainerSpacing, max_length=255, verbose_name='Vertical spacing'),
        ),
    ]
