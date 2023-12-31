from django.db import models


class ProgramingLanguageModel(models.Model):
    class IconType(models.TextChoices):
        FONT_AWSOME = "1", "FA"
        IMAGE = '2', 'image'

    name = models.CharField(max_length=50)
    icon_type = models.CharField(
        max_length=1,
        choices=IconType.choices,
        default=IconType.FONT_AWSOME
    )
    icon = models.TextField(help_text='fa ref or src ref')


class ToolModel(models.Model):

    class IconType(models.TextChoices):
        VIRTUAL = "1", "virtual"
        PHYSICAL = '2', 'physical'

