from django.apps import AppConfig
from django.db import models


class Bootstrap4Config(AppConfig):
    name = 'bootstrap4_alerts'
    verbose_name = 'Bootstrap 4 alerts'
    default_auto_field = models.AutoField
