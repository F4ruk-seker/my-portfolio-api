from django.db import models
from autoslug import AutoSlugField
# import string
# import random
from django.contrib.auth import get_user_model


User = get_user_model()


class ContentModel(models.Model):
    class LanguageType(models.TextChoices):
        ENG = "1", "English"
        TR = "2", "Türkçe"

    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title', unique=True)

    show = models.BooleanField(default=True)

    seo_description = models.CharField(max_length=500)
    seo_image_url = models.TextField(default=None, blank=True, null=True)
    seo_image_alt = models.TextField(blank=True, null=True)

    text = models.TextField(help_text='use html')

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('tags.TagModel', blank=True)
    content_type = models.ForeignKey('ContentTypeModel', on_delete=models.CASCADE)
    comments = models.ManyToManyField('ContentCommentModel', related_name='content', blank=True)

    view = models.ManyToManyField('analytical.ViewModel', blank=True, default=None, editable=True)

    language_type = models.CharField(max_length=1, choices=LanguageType, default=LanguageType.ENG)

    def get_view(self):
        return self.view.all()

    @property
    def banner(self):
        return self.seo_image_url

    def __str__(self):
        return f"Content ({self.id}) | {self.title} | {self.content_type.name} @{self.slug if self.slug else 'NEW'}"

    class Meta:
        ordering: tuple = 'title',


class ContentTypeModel(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    sub_tags = models.ManyToManyField('tags.TagCategoryModel', blank=True)


class ContentCommentModel(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=40, default=None, null=True)
    email = models.EmailField(max_length=40, default=None, null=True)
    # view
    sender_agent = models.ForeignKey('analytical.ViewModel', on_delete=models.CASCADE, default=None, null=True, blank=True, editable=True)
    # tracking = models.BooleanField(default=False)
    # disable_tracking_token = models.CharField(max_length=150, editable=False)

    comment = models.CharField(max_length=500)

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    '''
    @staticmethod
    def generate_random_disable_tracking_token(length: int = 150):
        pattern: str = string.ascii_letters + string.digits
        return ''.join(random.choices(population=pattern, k=length))

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.disable_tracking_token = self.generate_random_disable_tracking_token()
        super().save(*args, **kwargs)

    '''
