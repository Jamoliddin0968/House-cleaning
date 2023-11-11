from django.contrib import admin

from apps.services.models import Category, SubCategory

# Register your models here.


class SubCategoryInline(admin.TabularInline):
    model = SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline,]
