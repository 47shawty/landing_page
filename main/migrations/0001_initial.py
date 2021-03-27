# Generated by Django 3.1.7 on 2021-03-25 07:40

import ckeditor.fields
from django.db import migrations, models
import django_resized.forms
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[1280, 860], upload_to='uploads/product/%Y/%m/%d')),
                ('image_second', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[1280, 860], upload_to='uploads/product/%Y/%m/%d')),
                ('image_third', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, size=[1280, 860], upload_to='uploads/product/%Y/%m/%d')),
                ('description', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Header',
                'verbose_name_plural': 'Header',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, size=[1280, 1024], upload_to='uploads/product/%Y/%m/%d')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('first_list_title', models.CharField(max_length=50)),
                ('first_list', models.TextField()),
                ('second_list_title', models.CharField(max_length=50)),
                ('second_list', models.TextField()),
                ('third_list_title', models.CharField(max_length=50)),
                ('third_list', models.TextField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='SomeLocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
            ],
        ),
    ]
