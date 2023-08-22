from django.contrib import admin

from webstore.models import Product, Brand, Category, Basket
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ["name"]}
    
    
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ["name"]}
    
