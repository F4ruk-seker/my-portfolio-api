# Generated by Django 5.0.3 on 2024-05-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_alter_contentmodel_slug'),
        ('tags', '0002_tagcategorymodel_order_alter_tagcategorymodel_tags_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.tagmodel'),
        ),
    ]
