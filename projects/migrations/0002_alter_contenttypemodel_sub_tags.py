# Generated by Django 4.2.8 on 2024-02-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tagcategorymodel_order_alter_tagcategorymodel_tags_and_more'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttypemodel',
            name='sub_tags',
            field=models.ManyToManyField(blank=True, to='tags.tagcategorymodel'),
        ),
    ]
