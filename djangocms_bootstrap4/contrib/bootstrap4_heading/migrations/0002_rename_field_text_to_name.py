from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_heading', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bootstrap4heading',
            old_name='text',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='bootstrap4heading',
            name='name',
            field=models.TextField(max_length=2048, verbose_name='Text'),
        ),
    ]
