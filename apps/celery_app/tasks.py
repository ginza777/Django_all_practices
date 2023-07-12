from celery import shared_task
from django.contrib.auth.models import User
from faker import Faker

@shared_task
def add_fake_person():
    fake = Faker()
    name = fake.name()
    email = fake.email()
    User.objects.create(username=name, email=email)
    print(f"Yangi odam qo'shildi: {name}, {email}")
