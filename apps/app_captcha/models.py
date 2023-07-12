from django.db import models


class CaptchaUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="ism")
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name="parol")

    def __str__(self):
        return self.name
