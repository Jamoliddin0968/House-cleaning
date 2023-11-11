from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.services.models import Category, SubCategory
from apps.services.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListAPIView(ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = CategorySerializer


class SubCategoryDetailAPIView(RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = CategorySerializer
