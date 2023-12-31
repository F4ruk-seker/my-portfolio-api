# Generated by Django 4.2.8 on 2024-01-02 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_type', models.CharField(choices=[('I', 'Image'), ('V', 'Video')], default='I', max_length=2)),
                ('video_source_type', models.CharField(blank=True, choices=[('GD', 'Google Drive'), ('YT', 'Youtube'), ('CI', 'cloudinary')], max_length=2, null=True, verbose_name='Video Source Type')),
                ('url', models.TextField(help_text='allow only cdn')),
                ('alt', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('thumbnail', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaDirModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('media', models.ManyToManyField(to='media_manager.mediamodel')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media_manager.mediadirmodel')),
            ],
        ),
    ]
