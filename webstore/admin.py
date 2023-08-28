from django.contrib import admin

from webstore.models import Product, Brand, Category, Basket
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ["name"]}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ["name"]}

@admin.register(Brand)    
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_name": ["name"]}

