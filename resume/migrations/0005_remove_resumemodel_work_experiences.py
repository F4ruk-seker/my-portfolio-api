# Generated by Django 5.0.3 on 2024-04-07 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_workexperiencesmodel_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resumemodel',
            name='work_experiences',
        ),
    ]
