# Generated by Django 5.0.3 on 2024-09-11 06:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_alter_surveyuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='token',
            field=models.UUIDField(default=uuid.UUID('a490f072-f7d7-42cd-a6cb-4583097e7c44')),
        ),
    ]
