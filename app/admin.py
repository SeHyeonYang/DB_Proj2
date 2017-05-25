from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib import admin
from app.models import *
from django.apps import apps

for model in apps.get_app_config('app').models.values():
    admin.site.register(model)


