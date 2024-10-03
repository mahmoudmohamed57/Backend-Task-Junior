from rest_framework.pagination import PageNumberPagination

class CustomProductPagination(PageNumberPagination):
    page_size = 2
