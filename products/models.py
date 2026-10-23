from django.db import models
from category.models import Category

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank = True, null=True)
    description=models.TextField(max_length=1000)
    available=models.BooleanField(default=True)
    stock=models.IntegerField(default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

    def __str__(self):
        return self.name
    
