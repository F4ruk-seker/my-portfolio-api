# Generated by Django 5.0.3 on 2024-09-12 08:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_alter_surveyuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='token',
            field=models.UUIDField(default=uuid.UUID('93aabdaf-dbe0-4063-86c1-14fc8acced69')),
        ),
    ]
