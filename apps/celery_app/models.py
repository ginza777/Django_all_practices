from django.db import models

class YourModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    # Qo'shimcha maydonlar

    def __str__(self):
        return self.field1  # Ma'lumotni qaytarish uchun maydonni tanlang
