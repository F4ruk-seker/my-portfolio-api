# Generated by Django 5.0 on 2023-12-23 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_contextfieldmodel_field_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
