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


class Characteristic(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=500)
    value = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Review(models.Model):
    customer_name = models.CharField(max_length=500)
    review = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    review_number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    characteristics = models.ManyToManyField(Characteristic)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
