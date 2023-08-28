from rest_framework import serializers

from webstore.models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'category', 'image']
        read_only_fields = ['slug_name']