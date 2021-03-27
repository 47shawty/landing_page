from ckeditor.fields import RichTextField
from django_resized import ResizedImageField
from django.db import models
from mapbox_location_field.models import LocationField


class SomeLocationModel(models.Model):
    location = LocationField(map_attrs={
        "zoom": 7,
        "center": [41.26848144933652, 69.22686929378176],
        "cursor_style": 'pointer',
        "marker_color": "red",
        "rotate": True,
        "geocoder": True,
        "fullscreen_button": True,
        "navigation_buttons": True,
        "track_location_button": True,
        "readonly": True,
        "placeholder": "Pick a location on map below",
    })


class Header(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='uploads/home/%Y/%m/%d')
    image_second = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='uploads/home/%Y/%m/%d')
    image_third = ResizedImageField(size=[1280, 860], crop=['middle', 'center'], upload_to='uploads/home/%Y/%m/%d')
    description = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'


class ProductDetail(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[1280, 1024], crop=['middle', 'center'], upload_to='uploads/product/%Y/%m/%d')
    slug = models.SlugField(max_length=100, unique=True)
    first_list_title = models.CharField(max_length=50, blank=True, null=True)
    first_list = RichTextField(blank=True, null=True)
    second_list_title = models.CharField(max_length=50, blank=True, null=True)
    second_list = RichTextField(blank=True, null=True)
    third_list_title = models.CharField(max_length=50, blank=True, null=True)
    third_list = RichTextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
