from django.db import models


class MessageModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    sender_agent = models.ForeignKey(
        'analytical.ViewModel',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

