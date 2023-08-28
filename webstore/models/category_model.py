from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Category name')
    slug_name = models.SlugField(max_length=255, blank=False, null=False, unique=True, default='', verbose_name='Slug name')
    description = models.TextField(max_length=1020, blank=True, null=False, default='', verbose_name='Category description')
    
    class Meta:
        ordering = ['name', 'description']
    
    def __str__(self):
        return self.name