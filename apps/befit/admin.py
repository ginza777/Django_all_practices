from django.contrib import admin
from .models import Clients, Product, Review


# Register your models here.
@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'password', 'email', 'image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount', 'price', 'description', 'image', 'category')
    list_editable = ('discount', 'price', 'category')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('text', 'stars', 'username')

