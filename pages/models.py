from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField


class PageModel(models.Model):
    name = models.CharField(max_length=20, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # ceo
    keywords = models.TextField(blank=True, null=True)
    cloudinary_settings = {
        'overwrite': True,
        'folder': 'portfolyo/page/ceo',
        'resource_type': "image",
        'transformation': {"quality": "auto:low"},
        'format': "webp",
    }
    # image = models.ImageField(default=None, blank=True, null=True) if settings.DEBUG else CloudinaryField("image", **cloudinary_settings)
    image = models.TextField(default=None, blank=True)
    image_alt = models.TextField(blank=True, null=True)
    disable_ceo = models.BooleanField(default=False)

    context = models.ManyToManyField('pages.ContextFieldModel')

    view = models.ManyToManyField('analytical.ViewModel', blank=True,default=None,editable=True)

    def get_view(self):
        return self.view.all()


class ContextFieldModel(models.Model):
    class FieldType(models.TextChoices):
        MD = "1", "MD"
        LIST = "2", "List"
        IMG = '3', 'img'
        TEXT = '4', 'text'
        HTML = '5', 'html'

    name = models.SlugField(max_length=50, default=None, blank=True, null=True)
    field_type = models.CharField(
        max_length=2,
        choices=FieldType.choices,
        default=FieldType.MD
    )
    field_value = models.TextField()

    def get_field_value(self):
        if self.field_type == self.FieldType.LIST:
            return self.field_value.split(',')
        return self.field_value

    def __str__(self):
        return f'{self.name} - {self.field_type}'

