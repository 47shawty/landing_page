# Generated by Django 3.1.7 on 2021-03-25 07:49

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210325_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='somelocationmodel',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={}),
        ),
    ]