from django.contrib.auth.models import User
from django.db import models


class ResumeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    context = models.TextField()

