from rest_framework import serializers

from webstore.models import Brand

class BrandSerializer(serializers.Serializer):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'category']
        read_only_fields = ['slug_name']