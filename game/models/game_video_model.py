from autoslug import AutoSlugField
from django.db import models


class GameVideoModel(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    show = models.BooleanField(default=True)

    seo_description = models.CharField(max_length=500)
    seo_image_url = models.TextField(default=None, blank=True)
    seo_image_alt = models.TextField(blank=True, null=True)

    video = models.ForeignKey('media_manager.MediaModel', on_delete=models.CASCADE)
    # thumbnail = video is already has thumbnail field
    description = models.TextField(max_length=350)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('tags.TagModel')
    content_type = models.ForeignKey('projects.ContentTypeModel', on_delete=models.CASCADE)
    comments = models.ManyToManyField('projects.ContentCommentModel', related_name='game_videos', blank=True)

    view = models.ManyToManyField('analytical.ViewModel', blank=True, default=None, editable=True)

    def get_view(self):
        return self.view.all()

