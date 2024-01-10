# Generated by Django 4.2.8 on 2024-01-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_navbaritemmodel_navbarmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbaritemmodel',
            name='icon',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='navbaritemmodel',
            name='icon_position',
            field=models.CharField(blank=True, choices=[('start', 'Start'), ('end', 'End')], default=None, max_length=10),
        ),
    ]