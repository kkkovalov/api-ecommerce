from django.db import models
from django.conf import settings

from webstore.models import Category, Brand

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Product name',)
    description = models.TimeField(max_length=1020, verbose_name='Description')
    price = models.FloatField(blank=False, verbose_name='Price')
    stock_quantity = models.IntegerField(blank=False, default=0, null=False, verbose_name='In stock')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Product category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Product brand')
    # picture_url = 
    
    def __str__(self):
        return self.name
    
    def get_current_rating(self):
        pass
    
    def get_pictures(self):
        pass