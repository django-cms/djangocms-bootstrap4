from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0010_drop_field_spacing_vertical_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrap4gridrow',
            name='gutters_horizontal',
        ),
        migrations.AlterField(
            model_name='bootstrap4gridrow',
            name='gutters',
            field=models.BooleanField(default=False, help_text='Removes the horizontal spacing between the columns.', verbose_name='Remove gutters'),
        ),
    ]
