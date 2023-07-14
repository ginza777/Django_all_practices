from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'brend', 'model', 'type', 'image_url', 'description')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'price', 'brend', 'model', 'type', 'image_url', 'description')
    list_filter = ('title', 'price', 'brend', 'model', 'type', 'image_url', 'description')
    list_per_page = 25
