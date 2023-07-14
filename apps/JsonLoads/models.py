from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    stock = models.IntegerField()
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    thumbnail = models.URLField()
    images = models.JSONField()

    class Meta:
        verbose_name = 'ApiProducts'
        verbose_name_plural = 'ApiProducts'
        db_table = 'Apiproducts'

    def __str__(self):
        return self.title


class CartProducts(models.Model):

    cart_product_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'CartProducts'
        verbose_name_plural = 'CartProducts'
        db_table = 'cart_products'

    def __str__(self):
        return self.title


class Carts(models.Model):
    cart_id = models.IntegerField(primary_key=True)
    products = models.ManyToManyField(CartProducts)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_total = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.IntegerField()
    total_products = models.IntegerField()
    total_quantity = models.IntegerField()

    class Meta:
        verbose_name = 'Carts'
        verbose_name_plural = 'Carts'
        db_table = 'carts'

    def __str__(self):
        return str(self.user_id)


class ApiUsers(models.Model):
    fist_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=255)
    phone = PhoneNumberField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birth_date = models.DateField()
    image = models.URLField()
    blood_group = models.CharField(max_length=255)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    eye_color = models.CharField(max_length=255)
    hair_color = models.CharField(max_length=255)
    hair_type = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    address = models.JSONField()
    mac_address = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    bank = models.JSONField()
    company = models.JSONField()
    ein = models.CharField(max_length=255)
    ssn = models.CharField(max_length=255)
    user_agent = models.TextField()

    class Meta:
        verbose_name = 'ApiUsers'
        verbose_name_plural = 'ApiUsers'
        db_table = 'api_users'

    def __str__(self):
        return self.username


class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    user_id = models.IntegerField()
    tags = models.JSONField()
    reactions = models.IntegerField()

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'
        db_table = 'posts'

    def __str__(self):
        return self.title


class Comments(models.Model):
    body = models.TextField()
    post_id = models.IntegerField()
    user = models.JSONField()

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
        db_table = 'comments'

    def __str__(self):
        return self.body


class Images(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    images = models.ImageField(upload_to='images')
    extra = models.JSONField()

    class Meta:
        verbose_name = 'ApiImages'
        verbose_name_plural = 'ApiImages'
        db_table = 'Apiimages'

    def __str__(self):
        return self.title


class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.JSONField()
    likes = models.IntegerField()

    class Meta:
        verbose_name = 'Quotes'
        verbose_name_plural = 'Quotes'
        db_table = 'quotes'

    def __str__(self):
        return self.quote


class Todos(models.Model):
    todo = models.TextField()
    completed = models.BooleanField()
    user_id = models.IntegerField()

    class Meta:
        verbose_name = 'Todos'
        verbose_name_plural = 'Todos'
        db_table = 'todos'

    def __str__(self):
        return self.title
