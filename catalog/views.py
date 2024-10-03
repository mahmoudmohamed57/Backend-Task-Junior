from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomProductPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('subcategory__category')
    serializer_class = ProductSerializer
    pagination_class = CustomProductPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name']
