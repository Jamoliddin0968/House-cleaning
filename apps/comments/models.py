from django.db import models

from 
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey()
