import json
import requests
import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.JsonLoads.models import Posts
from apps.JsonLoads.views import UrlApi


def set_data(data: dict):
    with transaction.atomic():
        posts = Posts.objects.create(
            title=data["title"],
            body=data["body"],
            user_id=data["userId"],
            tags=data["tags"],
            reactions=data["reactions"],

        )
        posts.save()


class Command(BaseCommand):
    help = "Load products data from json file"

    def handle(self, *args, **kwargs):
        url = UrlApi.posts
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for post in data["posts"]:
                set_data(post)
            print('success')
        else:
            print("Error")
