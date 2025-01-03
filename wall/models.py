from django.db import models


class WallModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    wall = models.TextField()  # MD
    is_featured = models.BooleanField(default=False)
