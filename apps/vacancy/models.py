from django.db import models


# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/logo/', null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Vacancies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    salary = models.FloatField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')

    def __str__(self):
        return self.name


class Clients(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.fullname


class Resume(models.Model):
    name = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='resume')
    resume = models.FileField(upload_to='resume', null=True, blank=True)

    def __str__(self):
        return self.name
