from django.db import models


class MediaDirModel(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('MediaDirModel', on_delete=models.CASCADE)
    media = models.ManyToManyField('MediaModel')


class MediaModel(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "I", "Image"
        VIDEO = "V", "Video"

    class VideoSourceType(models.TextChoices):
        GOOGLE_DRIVE = "GD", "Google Drive"
        YOUTUBE = "YT", "Youtube"
        CLOUDINARY = "CI", "cloudinary"

    media_type = models.CharField(
        max_length=2,
        choices=MediaType.choices,
        default=MediaType.IMAGE
    )

    video_source_type = models.CharField(
        max_length=2,
        choices=VideoSourceType.choices,
        blank=True,
        null=True,
        verbose_name="Video Source Type"
    )

    url = models.TextField(help_text='allow only cdn')
    alt = models.CharField(max_length=200, default=None, blank=True, null=True)
    thumbnail = models.TextField(null=True, blank=True, default=None)

    def create_thumbnail(self):
        ...

    def save(self, *args, **kwargs):
        if self.media_type == self.MediaType.VIDEO and not self.video_source_type:
            self.video_source_type = self.VideoSourceType.GOOGLE_DRIVE
        super().save(*args, **kwargs)

