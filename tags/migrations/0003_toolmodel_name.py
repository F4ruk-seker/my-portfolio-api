# Generated by Django 4.2.8 on 2024-01-27 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_programinglanguagemodel_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='toolmodel',
            name='name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
    ]