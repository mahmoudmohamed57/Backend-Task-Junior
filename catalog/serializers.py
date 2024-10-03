from rest_framework import serializers
from .models import Product, Subcategory

class ProductSerializer(serializers.ModelSerializer):
    subcategory_id = serializers.IntegerField(write_only=True)
    subcategory_name = serializers.CharField(source='subcategory.name', read_only=True)
    category_name = serializers.CharField(source='subcategory.category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'subcategory_id', 'subcategory_name', 'category_name']
    
    def validate_subcategory_id(self, value):
        try:
            Subcategory.objects.get(id=value)
        except Subcategory.DoesNotExist:
            raise serializers.ValidationError("Invalid subcategory ID.")
        return value
