from .product_model import *

# Basic models of webstore


# [ ] - create a filesystem to hold pictures 
import os
from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Category name')
    description = models.TextField(max_length=1020, blank=True, null=False, default='', verbose_name='Category description')
    
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Brand name')
    # category = 
    description = models.TimeField(max_length=1020, verbose_name='Description')
    
    
class Pictures(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product")
    # picture_url =
    # picture_description/meta_data = 
    # when multiple or single picture(s) stored in filesystem they can be retrieved by Production function of get_pictures()
    
    def __str__(self):
        # return picture description or url
        pass

class Basket(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.IntegerField(blank=False, null=False, default=1, editable=True)
    
    def __str__(self):
        return self.user + 'basket'
    

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating_value = models.FloatField(blank=False, default=5.0, verbose_name='Rating value') # required, (1.0-5.0)
    text = models.TextField(blank=True, null=True, verbose_name='Rating text') # optional
    