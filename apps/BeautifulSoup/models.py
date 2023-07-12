from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    brend= models.CharField(max_length=200, null=True, blank=True)
    model= models.CharField(max_length=200, null=True, blank=True)
    type= models.CharField(max_length=200, null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class ProductLink(models.Model):
    link = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.link