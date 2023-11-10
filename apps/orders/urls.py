from django.urls import path

from apps.orders import views

urlpatterns = [
    path('create/', views.ContactCreateAPIView.as_view(), name="contact_create"),
]
