from django.contrib import admin
from . import models


admin.site.register(models.PageModel)
# admin.site.register(models.ContextModel)
admin.site.register(models.ContextFieldModel)
admin.site.register(models.NavbarModel)
admin.site.register(models.NavbarItemModel)