# Generated by Django 4.2.8 on 2024-01-04 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_contextfieldmodel_field_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NavbarItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('icon', models.CharField(max_length=50)),
                ('icon_position', models.CharField(choices=[('start', 'Start'), ('end', 'End')], max_length=10)),
                ('display_text_on_hover_pc', models.BooleanField(default=True)),
                ('hide_text_on_pc', models.BooleanField(default=False)),
                ('hide_text_on_mobile', models.BooleanField(default=True)),
                ('navbar_item_position', models.CharField(choices=[('start', 'Start'), ('center', 'Center'), ('end', 'End')], max_length=10)),
                ('url_type', models.CharField(choices=[('hashtag', 'Hashtag'), ('internal', 'Internal'), ('external', 'External')], max_length=20)),
                ('internal_url', models.CharField(blank=True, max_length=255, null=True)),
                ('external_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavbarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('items', models.ManyToManyField(to='pages.navbaritemmodel')),
            ],
        ),
    ]
