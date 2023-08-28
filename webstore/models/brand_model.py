from django.db import models
from webstore.models import Category
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save


        
class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False, verbose_name='Brand name')
    slug_name = models.SlugField(max_length=255, blank=False, null=False, verbose_name="Slug name", unique=True)
    description = models.TextField(max_length=1020, verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Brand image', upload_to='brands/',default=None)
    
    def __str__(self):
        return self.name
    
    
# @receiver(pre_save, sender=Brand)
# def pre_save_image_name(sender, instance, *args, **kwargs):
#     if instance.image is not None:
#         instance.image.name = i