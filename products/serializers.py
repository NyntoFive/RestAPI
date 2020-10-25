from rest_framework import serializers
from products.models import CKKItem

class CKKItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CKKItem
        fields = ['id', 'name', 'sku', 'description', 'image', 'price', 'digital']