from rest_framework import serializers, pagination

from .models import Item, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('name',)


class ItemSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()  
    
    class Meta:
        model = Item
        fields = (
            'name',
            'category',
            'sale_price',
        )
        
class ItemPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
    

class ItemDetailSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()  
    
    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'category',
            'sale_price',
            'stock'
        )