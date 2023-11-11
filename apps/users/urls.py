# users url py
from django.urls import path

from apps.users import views

urlpatterns = [

    path('profil/', views.UserAPIView.as_view(), name='user_detail'),

]
