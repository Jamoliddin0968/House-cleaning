from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.comments.serializers import CommentSerializer
from apps.services.models import Category, SubCategory


class SubCategorySerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SubCategory


class CategorySerializer(ModelSerializer):
    subcategories = SubCategorySerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Category
