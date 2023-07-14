import json
import requests
import requests
from django.core.management.base import BaseCommand
from django.db import transaction

from apps.JsonLoads.models import Comments
from apps.JsonLoads.views import UrlApi


def set_data(data: dict):
    with transaction.atomic():
        comments = Comments.objects.create(
            body=data["body"],
            post_id=data["postId"],
            user=data["user"]


        )
        comments.save()


class Command(BaseCommand):
    help = "Load products data from json file"

    def handle(self, *args, **kwargs):
        url = UrlApi.comments
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for comment in data["comments"]:
                set_data(comment)
            print('success')
        else:
            print("Error")
