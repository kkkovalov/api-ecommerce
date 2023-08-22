from django.db import models
from django.conf import settings

from webstore.models import Category, Brand

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product name', blank=False, null=False)
    slug_name = models.SlugField(verbose_name='Slug name', max_length=255, blank=False, null=False)
    type = models.CharField(max_length=255, verbose_name='Type of product', blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Product category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Product brand')
    data = models.JSONField(max_length=255, verbose_name="Custom data", blank=True, null=True)
    description = models.TimeField(max_length=1020, verbose_name='Description', blank=False, null=False)
    price = models.FloatField(verbose_name='Price', blank=False, null=False)
    stock_quantity = models.IntegerField(blank=False,verbose_name='In stock', default=0, null=False)
    picture_url = models.URLField(max_length=255, verbose_name="Picture URL", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def get_current_rating(self):
        pass