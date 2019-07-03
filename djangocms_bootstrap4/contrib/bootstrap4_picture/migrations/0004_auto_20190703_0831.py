# Generated by Django 2.2.2 on 2019-07-03 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_picture', '0003_auto_20181212_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='caption_text',
            field=models.TextField(blank=True, help_text='Provide a description, attribution, copyright or other information.', null=True, verbose_name='Caption text'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='external_picture',
            field=models.URLField(blank=True, help_text='If provided, overrides the embedded image. Certain options such as cropping are not applicable to external images.', max_length=255, null=True, verbose_name='External image'),
        ),
        migrations.AlterField(
            model_name='bootstrap4picture',
            name='link_url',
            field=models.URLField(blank=True, help_text='Wraps the image in a link to an external URL.', max_length=2040, null=True, verbose_name='External URL'),
        ),
    ]
