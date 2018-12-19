from django.contrib import admin
from django.apps import apps
from .models import Language


app = apps.get_app_config('semstew')

for model_name, model in app.models.items():
    admin.site.register(model)

