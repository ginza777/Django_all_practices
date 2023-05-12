from django.db import models


# Create your models here.

# foydalanuvchilar
class Clients(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username


# foydanaluvchilar  komentariyasi
class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField()
    username = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} - {self.stars}"


# mahsulotlar

class Product(models.Model):
    title = models.CharField(max_length=100)
    discount = models.IntegerField(null=True, blank=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
