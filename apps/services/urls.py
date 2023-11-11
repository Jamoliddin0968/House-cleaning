# users url py
from django.urls import path

from apps.services import views

urlpatterns = [
    path('category/all', views.CategoryListAPIView.as_view(), name="categories"),
    path('category/<int:pk>', views.CategoryDetailAPIView.as_view(),
         name="category_detail"),
    path('subcategory/all', views.CategoryListAPIView.as_view(), name="subcategories"),
    path('subcategory/<int:pk>', views.CategoryDetailAPIView.as_view(),
         name="subcategory_detail"),
]
