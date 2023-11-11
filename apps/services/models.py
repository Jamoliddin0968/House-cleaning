from django.db import models

# Create your models here.


class Category(models.Model):
    name_uz = models.CharField(max_length=31)
    name_ru = models.CharField(max_length=31)
    name_en = models.CharField(max_length=31)

    img = models.ImageField(upload_to="category/")


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=31)
    name_ru = models.CharField(max_length=31)
    name_en = models.CharField(max_length=31)

    summary_uz = models.CharField(max_length=255)
    summary_ru = models.CharField(max_length=255)
    summary_en = models.CharField(max_length=255)
    img = models.ImageField(upload_to="subcategory/")
    video = models.FileField(upload_to='videos/')
    description_uz = models.TextField()
    description_ru = models.TextField()
    description_en = models.TextField()
