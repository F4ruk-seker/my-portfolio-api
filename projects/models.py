from django.db import models
from autoslug import AutoSlugField

from django.contrib.auth import get_user_model

User = get_user_model()


class ContentModel(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    ceo_description = models.CharField(max_length=500)
    ceo_image_url = models.TextField(default=None, blank=True)
    ceo_image_alt = models.TextField(blank=True, null=True)

    text = models.TextField(help_text='use html')

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('tags.TagModel')
    content_type = models.ForeignKey('ContentTypeModel', on_delete=models.CASCADE)
    comments = models.ManyToManyField('ContentCommentModel', related_name='content')


class ContentTypeModel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    sub_tags = models.ManyToManyField('tags.TagCategoryModel', blank=True)


class ContentCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
