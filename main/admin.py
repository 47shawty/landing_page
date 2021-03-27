from django.contrib import admin
from . import models

from .models import SomeLocationModel
from mapbox_location_field.admin import MapAdmin

admin.site.register(SomeLocationModel, MapAdmin)


@admin.register(models.Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'id'
    ]


@admin.register(models.ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
