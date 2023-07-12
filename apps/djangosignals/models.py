from django.db import models
import random
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver
from django.conf import settings
import os

User = get_user_model()


class Images(models.Model):
    title = models.CharField(max_length=255, default='title')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'images'
        verbose_name_plural = 'Images'

    def __str__(self):
        return f'{self.created_at}'


class ProductShop(models.Model):
    name = models.CharField(max_length=255, default='product', blank=True)
    image = models.FileField(upload_to='images/')
    images = models.ManyToManyField('Images', related_name='product')
    short_description = models.TextField(default='product', blank=True)
    description = models.TextField(default='product', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    product_code = models.BigIntegerField(null=True, blank=True, unique=True,
                                          default=random.randint(1000000000, 9999999999))
    count_of_product = models.IntegerField(default=1, blank=True)
    sold_count = models.IntegerField(default=0, blank=True)
    discount = models.IntegerField(default=0, blank=True)
    liked = models.ManyToManyField(User, related_name='liked', blank=True)
    category = models.ManyToManyField('Category', related_name='products', blank=True)
    shop = models.ForeignKey('Shop', related_name="shop", on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name


class ShopAssistant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, default='shop_assistant')

    class Meta:
        db_table = 'shop_assistant'
        verbose_name_plural = 'Shop_assistant'

    def __str__(self):
        return f"{self.user}"


class Shop(models.Model):
    shop_assistant = models.ForeignKey(ShopAssistant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='shop')
    description = models.TextField(default='shop')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    document = models.FileField(upload_to='documents/')

    class Meta:
        db_table = 'shops'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, default='category')

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# logwriter function
def logwriter(sender, instance, method: str):
    log_file_path = os.path.join(settings.BASE_DIR, f'apps/djangosignals/logs/log_{method}.txt')
    try:
        with open(log_file_path, 'a+') as file:
            field_values = []
            for field in instance._meta.fields:
                field_name = field.name
                field_value = getattr(instance, field_name)
                field_values.append(f"{field_name}: {field_value}")

            # Join field values into a single string
            fields_text = "\n".join(field_values)

            text = f"The product '{instance.name}' was created.\n" \
                   f"Sender: {sender}\n" \
                   f"Instance ID: {instance.pk}\n" \
                   f"Fields:\n{fields_text}"
            file.write(text + '\n')
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")


# signals
@receiver(pre_save, sender=ProductShop)
def product_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_save_ProductShop')


@receiver(post_save, sender=ProductShop)
def product_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_save_ProductShop')


@receiver(pre_delete, sender=ProductShop)
def product_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_delete_ProductShop')


@receiver(post_delete, sender=ProductShop)
def product_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_delete_ProductShop')


@receiver(pre_save, sender=ShopAssistant)
def shop_assistant_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_save_Shop_assistant')


@receiver(post_save, sender=ShopAssistant)
def shop_assissant_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_save_Shop_assistant')


@receiver(pre_delete, sender=ShopAssistant)
def shop_assisssant_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_delete_Shop_assistant')


@receiver(post_delete, sender=ShopAssistant)
def shop_assisssant_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_delete_Shop_assistant')


@receiver(pre_save, sender=Shop)
def shop_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_save_Shop')


@receiver(post_save, sender=Shop)
def shop_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_save_Shop')


@receiver(pre_delete, sender=Shop)
def shop_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_delete_Shop')


@receiver(post_delete, sender=Shop)
def shop_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_delete_Shop')


@receiver(pre_save, sender=Images)
def product_description_images_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_save_images')


@receiver(post_save, sender=Images)
def product_description_images_created(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_save_images')


@receiver(pre_delete, sender=Images)
def product_description_images_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'pre_delete_images')


@receiver(post_delete, sender=Images)
def product_description_images_deleted(sender, instance,**kwargs):
    logwriter(sender, instance, 'post_delete_images')
