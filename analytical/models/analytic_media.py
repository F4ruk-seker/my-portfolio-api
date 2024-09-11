from django.db import models


class AnalyticMedia(models.Model):
    view = models.ManyToManyField('analytical.ViewModel', blank=True, default=None, editable=True)
    platform_host = models.CharField(max_length=150)
    platform_path = models.TextField(default='')
    media_source = models.TextField(default='')
