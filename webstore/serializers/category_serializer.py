from rest_framework import serializers

from webstore.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "description", "slug_name"]
        read_only_fields = ["slug_name"]
        