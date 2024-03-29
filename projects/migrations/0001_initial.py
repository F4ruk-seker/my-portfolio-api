# Generated by Django 4.2.8 on 2024-01-30 18:40

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTypeModel',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('sub_tags', models.ManyToManyField(to='tags.tagmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ContentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('ceo_description', models.CharField(max_length=500)),
                ('ceo_image_url', models.TextField(blank=True, default=None)),
                ('ceo_image_alt', models.TextField(blank=True, null=True)),
                ('text', models.TextField(help_text='use html')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.contenttypemodel')),
                ('tags', models.ManyToManyField(to='tags.tagmodel')),
            ],
        ),
    ]
