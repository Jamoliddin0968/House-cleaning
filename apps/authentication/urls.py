# users url py
from django.urls import path

from apps.authentication import views

urlpatterns = [
    path('sign_up/', views.PhoneNumberAuthAPIView.as_view(), name="sign_up"),
    path('verify_code/', views.VerifyCodeAPIView.as_view(), name="verify_code"),
    path('re_send/', views.PhoneNumberAuthAPIView.as_view(), name='re_send'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]
