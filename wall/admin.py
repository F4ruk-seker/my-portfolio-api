from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import WallModel


admin.site.register(WallModel, ModelAdmin)
