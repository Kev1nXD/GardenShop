from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductCriterion(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    criterion = models.ForeignKey(ProductCriterion, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    postal_code = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    
    def __str__(self):
        return self.id
