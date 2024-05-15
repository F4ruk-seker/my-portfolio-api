# Generated by Django 5.0.3 on 2024-05-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectExperiencesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('link', models.URLField(blank=True, default=None, null=True)),
                ('experience', models.TextField()),
                ('show', models.BooleanField(default=True)),
                ('project_type', models.CharField(choices=[('HB', 'Hobby'), ('OS', 'open source'), ('DP', 'Development'), ('CB', 'Contribution')], default='OS', max_length=2)),
            ],
        ),
    ]
