import json
import requests
import requests
from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.JsonLoads.models import Products
from apps.JsonLoads.views import UrlApi


def set_data(data: dict):
    with transaction.atomic():
        products = Products.objects.create(
            product_id=data["id"],
            title=data["title"],
            description=data["description"],
            price=data["price"],
            discount_percentage=data["discountPercentage"],
            rating=data["rating"],
            stock=data["stock"],
            brand=data["brand"],
            category=data["category"],
            thumbnail=data["thumbnail"],
            images=data["images"]
        )
        products.save()


class Command(BaseCommand):
    help = "Load products data from json file"

    def handle(self, *args, **kwargs):
        url = UrlApi.products
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for product in data["products"]:
                set_data(product)
        else:

            print(data['total'])
            print(data['skip'])
            print(data['limit'])
