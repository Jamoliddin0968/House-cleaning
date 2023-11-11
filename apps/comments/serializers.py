# from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.comments.models import Comment
from apps.users.serializers import UserSerializer


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        exclude = ("id",)
