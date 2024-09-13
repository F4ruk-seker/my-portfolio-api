from unfold.admin import ModelAdmin
from django.contrib import admin
from . import models

admin.site.register(models.MediaModel, ModelAdmin)
admin.site.register(models.MediaDirModel, ModelAdmin)

