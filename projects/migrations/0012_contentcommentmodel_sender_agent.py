# Generated by Django 5.0.3 on 2024-05-01 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytical', '0004_viewmodel_time_tick_count'),
        ('projects', '0011_remove_contentcommentmodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentcommentmodel',
            name='sender_agent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='analytical.viewmodel'),
        ),
    ]
