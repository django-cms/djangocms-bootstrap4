from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_grid', '0003_migrate_column_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrap4gridcolumn',
            name='column_size',
        ),
    ]
