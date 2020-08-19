from django.db import migrations
from django.db.models import F, Func, Value
from django.db.models.functions import Concat


def forwards_func(apps, schema_editor):  # pragma: no cover
    icon = apps.get_model('bootstrap4_link', 'Bootstrap4Link')

    icon.objects.filter(icon_left__startswith='el-icon-').update(icon_left=Concat(Value('el '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='flag-icon-').update(icon_left=Concat(Value('flag-icon '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='fa-').update(icon_left=Concat(Value('fa '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='glyphicon-').update(icon_left=Concat(Value('glyphicon '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='ion-').update(icon_left=Concat(Value('ion '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='map-icon-').update(icon_left=Concat(Value('map-icon '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='zmdi-').update(icon_left=Concat(Value('zmdi '), 'icon_left'))
    icon.objects.filter(icon_left__startswith='wi-').update(icon_left=Concat(Value('wi '), 'icon_left'))

    icon.objects.filter(icon_right__startswith='el-icon-').update(icon_right=Concat(Value('el '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='flag-icon-').update(icon_right=Concat(Value('flag-icon '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='fa-').update(icon_right=Concat(Value('fa '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='glyphicon-').update(icon_right=Concat(Value('glyphicon '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='ion-').update(icon_right=Concat(Value('ion '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='map-icon-').update(icon_right=Concat(Value('map-icon '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='zmdi-').update(icon_right=Concat(Value('zmdi '), 'icon_right'))
    icon.objects.filter(icon_right__startswith='wi-').update(icon_right=Concat(Value('wi '), 'icon_right'))

def reverse_func(apps, schema_editor):  # pragma: no cover
    icon = apps.get_model('bootstrap4_link', 'Bootstrap4Link')

    icon.objects.filter(icon_left__startswith='el ').update(icon_left=Func(F('icon_left'), Value('el '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='flag-icon ').update(icon_left=Func(F('icon_left'), Value('flag-icon '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='fa ').update(icon_left=Func(F('icon_left'), Value('fa '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='glyphicon ').update(icon_left=Func(F('icon_left'), Value('glyphicon '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='map-icon ').update(icon_left=Func(F('icon_left'), Value('map-icon '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='zmdi ').update(icon_left=Func(F('icon_left'), Value('zmdi '), Value(''), function='replace',))
    icon.objects.filter(icon_left__startswith='wi ').update(icon_left=Func(F('icon_left'), Value('wi '), Value(''), function='replace',))

    icon.objects.filter(icon_right__startswith='el ').update(icon_right=Func(F('icon_right'), Value('el '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='flag-icon ').update(icon_right=Func(F('icon_right'), Value('flag-icon '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='fa ').update(icon_right=Func(F('icon_right'), Value('fa '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='glyphicon ').update(icon_right=Func(F('icon_right'), Value('glyphicon '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='map-icon ').update(icon_right=Func(F('icon_right'), Value('map-icon '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='zmdi ').update(icon_right=Func(F('icon_right'), Value('zmdi '), Value(''), function='replace',))
    icon.objects.filter(icon_right__startswith='wi ').update(icon_right=Func(F('icon_right'), Value('wi '), Value(''), function='replace',))


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap4_link', '0002_add_icons'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
