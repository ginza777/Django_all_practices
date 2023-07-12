import random

from django.db import models


# Create your models here.

def default_gender():
    Gender = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    return random.choice(Gender)[0]
class Fakeuser(models.Model):
    Gender = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    job = models.CharField(max_length=500)
    live_city = models.CharField(max_length=500)
    married = models.BooleanField(default=False)
    language = models.CharField(max_length=500)
    latutude = models.CharField(max_length=500)
    longitude = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    image = models.ImageField(upload_to='fakeimages/')
    gender = models.CharField(max_length=500, choices=Gender, default=default_gender)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fakeuser'
        verbose_name_plural = 'Fakeusers'
