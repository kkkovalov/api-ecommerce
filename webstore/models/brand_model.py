from django.db import models
from webstore.models import Category

class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Brand name')
    slug_name = models.SlugField(max_length=255, blank=False, null=False, verbose_name="Slug name", unique=True)
    description = models.TextField(max_length=1020, verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture_url = models.URLField(max_length=255, blank=True, null=True, verbose_name='Picture URL')
    
    def __str__(self):
        return self.name
    
    # def get_picture(self):
        # return self.picture_url
    