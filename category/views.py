from django.shortcuts import render
from rest_framework import viewsets
from category.models import Category
from category.serializers import CatagorySerializer

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CatagorySerializer
    lookup_field ="slug"

