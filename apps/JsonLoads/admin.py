from django.contrib import admin

# Register your models here.
from apps.JsonLoads.models import Products, ApiUsers,Posts,Comments,CartProducts,Carts

admin.site.register(Products)
admin.site.register(ApiUsers)
admin.site.register(Posts)
admin.site.register(Comments)
@admin.register(CartProducts)
class CartProductsAdmin(admin.ModelAdmin):
    list_display=(

        'cart_product_id',
        'title',
        'price',
        'quantity',
        'total',
        'discount_percentage',
        'discount_price',
    )

@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display=(
        'cart_id',
        'total',
        'discounted_total',
        'user_id',
        'total_products',
        'total_quantity',
    )
