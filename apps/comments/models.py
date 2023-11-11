from django.db import models

from apps.services.models import Category
from apps.users.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comment = models.CharField(max_length=127)
    rating = models.IntegerField()
