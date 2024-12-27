# Generated by Django 5.1.1 on 2024-12-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_alter_pagemodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel',
            name='context',
            field=models.ManyToManyField(blank=True, to='pages.contextfieldmodel'),
        ),
        migrations.AlterField(
            model_name='pagemodel',
            name='image',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]