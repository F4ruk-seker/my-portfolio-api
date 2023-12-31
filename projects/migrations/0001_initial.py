# Generated by Django 5.0 on 2023-12-31 04:30

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('ceo_description', models.CharField(max_length=500)),
                ('ceo_image_url', models.TextField(blank=True, default=None)),
                ('ceo_image_alt', models.TextField(blank=True, null=True)),
                ('context', models.TextField(help_text='use html')),
                ('programing_languages', models.ManyToManyField(to='tags.programinglanguagemodel')),
                ('used_tools', models.ManyToManyField(to='tags.toolmodel')),
            ],
        ),
    ]
