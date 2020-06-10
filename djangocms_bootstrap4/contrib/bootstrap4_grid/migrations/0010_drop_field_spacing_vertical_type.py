from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0009_add_fields_gutters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrap4gridcontainer',
            name='spacing_vertical_type',
        ),
    ]
