from django.db import models
from autoslug import AutoSlugField


class ProjectModel(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    ceo_description = models.CharField(max_length=500)
    ceo_image_url = models.TextField(default=None, blank=True)
    ceo_image_alt = models.TextField(blank=True, null=True)

    context = models.TextField(help_text='use html')

    programing_languages = models.ManyToManyField('tags.ProgramingLanguageModel')
    used_tools = models.ManyToManyField('tags.ToolModel')

    created = models.DateTimeField(auto_now_add=True)
