from django.db import models


class AnalyticMedia(models.Model):
    view = models.ManyToManyField('analytical.ViewModel', blank=True, default=None, editable=True)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, auto_created=True, blank=True, editable=True)
    platform_host = models.CharField(max_length=150)
    platform_path = models.TextField(default='')
    media_source = models.TextField(default='')
