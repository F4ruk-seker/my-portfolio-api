# Generated by Django 5.0.3 on 2024-08-09 07:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_surveyuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('url', models.URLField(blank=True, default=None, null=True)),
                ('color', models.CharField(help_text='hex, rgb, rgba', max_length=20)),
                ('icon', models.ImageField(upload_to='media/platform')),
            ],
        ),
        migrations.AlterField(
            model_name='surveyuser',
            name='token',
            field=models.UUIDField(default=uuid.UUID('996e8bbc-9b32-492e-bffc-fe9f24eb3d26')),
        ),
    ]
