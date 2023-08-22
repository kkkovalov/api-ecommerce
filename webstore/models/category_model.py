from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Category name')
    slug_name = models.SlugField(max_length=255, blank=False, null=False, unique=True, verbose_name='Slug name', default='')
    description = models.TextField(max_length=1020, blank=True, null=False, default='', verbose_name='Category description')
    
    class Meta:
        ordering = ['name', 'description']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name)
        return super().save(*args, **kwargs)