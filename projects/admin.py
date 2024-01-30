from django.contrib import admin
from . import models


admin.site.register(models.ContentModel)
admin.site.register(models.ContentTypeModel)

