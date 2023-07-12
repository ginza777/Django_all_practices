from django.contrib import admin
from .models import ProductShop, Shop, ShopAssistant, Images, Category


@admin.register(ProductShop)
class ProductShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'product_code']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']


@admin.register(ShopAssistant)
class ShopAssistantAdmin(admin.ModelAdmin):
    list_display = ['user', 'position']


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'image']
