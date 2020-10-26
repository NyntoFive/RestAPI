from rest_framework import serializers
from products.models import CKKItem

class CKKItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CKKItem
        fields = [
            "id",
            "name",
            "sku",
            "crawl_date",
            "date_str",
            "description",
            "desc_text",
            "price",
            "metaKeywords",
            "breadcrumbs",
            "image",
            "images",
            "category",
            "subcategory"]