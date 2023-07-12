import random

from django.core.management.base import BaseCommand
from faker import Faker

from apps.Fakeuser.models import Fakeuser

Gender = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
]


class Command(BaseCommand):
    help = "Create fake users"

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, help="Indicates the number of users to be created")

    def handle(self, *args, **kwargs):
        total = kwargs["total"]
        fake = Faker()
        for i in range(total):
            user = Fakeuser.objects.create(
                name=fake.name(),
                email=fake.email(),
                address=fake.address(),
                phone=fake.phone_number(),
                job=fake.job(),
                live_city=fake.city(),
                married=random.choice([True, False]),
                language=fake.language_code(),
                latutude=fake.latitude(),
                longitude=fake.longitude(),
                username=fake.user_name(),
                password=fake.password(),
                image=fake.image_url(),
                gender=random.choice(Gender)[0]
            )
            user.save()
            print(f"{i} - {user.name} fake user created {user.gender}")
        print("Fake user created successfully")
