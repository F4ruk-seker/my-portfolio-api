from django.db import models


class ToDoModel(models.Model):
    task = models.CharField(max_length=250)
    is_to_do = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
