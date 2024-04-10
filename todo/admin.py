from django.contrib import admin
from todo.models import ToDoModel, ToDoCategoryModel


admin.site.register(ToDoModel)
admin.site.register(ToDoCategoryModel)

