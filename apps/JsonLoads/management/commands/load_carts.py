import json
import requests
import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.JsonLoads.models import Carts,CartProducts
from apps.JsonLoads.views import UrlApi





def set_data(data: dict):
    if Carts.objects.filter(cart_id=data["id"]).exists():
        return Carts.objects.get(
            cart_id=data["id"],
            total=data["total"],
            discounted_total=data["discountedTotal"],
            user_id=data["userId"],
            total_products=data["totalProducts"],
            total_quantity=data["totalQuantity"],
            products=data["products"],
        )
    else:
        with transaction.atomic():
            cart_item = Carts.objects.create(
                cart_id=data["id"],
                total=data["total"],
                discounted_total=data["discountedTotal"],
                user_id=data["userId"],
                total_products=data["totalProducts"],
                total_quantity=data["totalQuantity"],

            )
            products=data.get("products",[])
            print(products)
            for product in products:
                if CartProducts.objects.filter(cart_product_id=product["id"]).exists():
                    product1 = CartProducts.objects.get(
                        cart_product_id=product["id"],
                    )
                    cart_item.products.add(product1)
                else:
                    with transaction.atomic():
                        product2 = CartProducts.objects.create(
                            cart_product_id=product["id"],
                            title=product["title"],
                            price=product["price"],
                            quantity=product["quantity"],
                            total=product["total"],
                            discount_percentage=product["discountPercentage"],
                            discount_price=product["discountedPrice"],

                        )
                        product2.save()
                        cart_item.products.add(product2)
            cart_item.save()


class Command(BaseCommand):
    help = "Load products data from json file"

    def handle(self, *args, **kwargs):
        url = UrlApi.carts
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for cart in data["carts"]:
                set_data(cart)
            print('success')
        else:
            print("Error")
