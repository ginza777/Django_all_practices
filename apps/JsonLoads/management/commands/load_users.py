import json
import requests
import requests
from django.core.management.base import BaseCommand
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.JsonLoads.models import ApiUsers
from apps.JsonLoads.views import UrlApi


def set_data(data: dict):
    with transaction.atomic():
        apiusers = ApiUsers.objects.create(
            fist_name=data["firstName"],
            last_name=data["lastName"],
            middle_name=data["maidenName"],
            age=data["age"],
            gender=data["gender"],
            email=data["email"],
            phone=data["phone"],
            username=data["username"],
            password=data["password"],
            birth_date=data["birthDate"],
            image=data["image"],
            blood_group=data["bloodGroup"],
            height=data["height"],
            weight=data["weight"],
            eye_color=data["eyeColor"],
            hair_color=data["hair"]["color"],
            hair_type=data["hair"]["type"],
            domain=data["domain"],
            ip_address=data["ip"],
            address=data["address"],
            mac_address=data["macAddress"],
            university=data["university"],
            bank=data["bank"],
            company=data["company"],
            ein=data["ein"],
            ssn=data["ssn"],
            user_agent=data["userAgent"]

        )
        apiusers.save()


class Command(BaseCommand):
    help = "Load products data from json file"

    def handle(self, *args, **kwargs):
        url = UrlApi.users
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for product in data["users"]:
                set_data(product)
            print("success")
        else:
            print("error")
