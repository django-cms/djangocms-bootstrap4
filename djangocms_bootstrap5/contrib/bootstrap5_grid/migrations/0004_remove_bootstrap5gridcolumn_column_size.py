from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap5_grid', '0003_migrate_column_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bootstrap5gridcolumn',
            name='column_size',
        ),
    ]
