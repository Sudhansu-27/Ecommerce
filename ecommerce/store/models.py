from distutils.command.upload import upload
from email.mime import image
from unicodedata import category, name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    
class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,related_name='subcategories', on_delete = models.CASCADE)
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category , related_name='products' , on_delete=models.CASCADE)
    subCategory = models.ForeignKey(SubCategory , related_name='products' , on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField()
    amount_in_stock = models.PositiveIntegerField()
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name = 'images' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImages/')     