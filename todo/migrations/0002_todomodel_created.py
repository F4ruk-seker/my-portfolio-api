# Generated by Django 4.2.8 on 2024-02-08 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]