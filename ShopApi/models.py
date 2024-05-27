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


# class Review(models.Model):
#     # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
#     customer_name = models.CharField(max_length=500, default='Анонім')
#     review = models.TextField()



class Color(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.height}см x {self.width}см x {self.weight}кг'


class Product(models.Model):
    name = models.CharField(max_length=500, unique=True)
    description = models.TextField(blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    review_number = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True)
    customer_name = models.CharField(max_length=500, default='Анонім')
    review = models.TextField()

    def __str__(self):
        return f'Review by {self.customer_name} for {self.product.name}'


