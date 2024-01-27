from django.db import models


class ProgramingLanguageModel(models.Model):
    class IconType(models.TextChoices):
        FONT_AWESOME = "1", "FA"
        IMAGE = '2', 'image'

    name = models.CharField(max_length=50)
    icon_type = models.CharField(
        max_length=1,
        choices=IconType.choices,
        default=IconType.FONT_AWESOME
    )
    icon = models.TextField(help_text='when call (fa/src) use this refs')


class ToolModel(models.Model):
    name = models.CharField(max_length=50)

    class IconType(models.TextChoices):
        VIRTUAL = "1", "virtual"
        PHYSICAL = '2', 'physical'

