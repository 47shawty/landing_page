# Generated by Django 3.1.7 on 2021-03-25 07:46

from django.db import migrations
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210325_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='somelocationmodel',
            name='location',
            field=mapbox_location_field.models.LocationField(map_attrs={'center': [41.311081, 69.240562]}),
        ),
    ]
