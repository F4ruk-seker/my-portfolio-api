# Generated by Django 5.0.3 on 2024-09-11 06:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_surveyuser_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyuser',
            name='token',
            field=models.UUIDField(default=uuid.UUID('7ce40ab6-bae9-4de3-8341-b3d0997e6401')),
        ),
    ]
