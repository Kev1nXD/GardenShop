from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500, unique=True)
    
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=500, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    TYPE_CHOICES = [
        ('width', 'Ширина'),
        ('height', 'Висота'),
        ('weight', 'Вага'),
        ('color', 'Колір'),
        ('size', 'Об\'єм'),
        ('Country manufacturer', 'Країна виробник'),

    ]
    type = models.CharField(max_length=500, choices=TYPE_CHOICES)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.type


class Review(models.Model):
    customer_name = models.CharField(max_length=500, default='Анонім')
    review = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    review_number = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    characteristics = models.ManyToManyField(Characteristic)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='images/')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.name
