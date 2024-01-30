# Generated by Django 4.2.8 on 2024-01-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('icon_type', models.CharField(choices=[('1', 'FA'), ('2', 'image')], default='1', max_length=1)),
                ('icon', models.TextField(help_text='when call (fa/src) use this refs')),
            ],
        ),
        migrations.CreateModel(
            name='TagCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tags', models.ManyToManyField(to='tags.tagmodel')),
            ],
        ),
    ]
