from django.contrib import admin
from todo.models import ToDoModel, ToDoCategoryModel
from unfold.admin import ModelAdmin


admin.site.register(ToDoModel, ModelAdmin)
admin.site.register(ToDoCategoryModel, ModelAdmin)

