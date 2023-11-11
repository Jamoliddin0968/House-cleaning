from django.contrib import admin

from .models import Category,SubCategory

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_uz',"name_ru","name_en"]
    list_editable = ["name_ru","name_en"]

admin.site.register(Category,CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_uz',"name_ru","name_en"]
    list_editable = ["name_ru","name_en"]
admin.site.register(SubCategory,SubCategoryAdmin)