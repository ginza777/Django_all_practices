from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

class YourModel(models.Model):
    content = RichTextField()
    # Qo'shimcha maydonlar
