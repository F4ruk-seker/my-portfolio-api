from django.contrib import admin
from . import models

admin.site.register(models.MediaModel)
admin.site.register(models.MediaDirModel)

