from django.db import models


class MessageModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

