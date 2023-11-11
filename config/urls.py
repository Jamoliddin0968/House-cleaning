"""
    Asosit url fayl
"""
from django.contrib import admin
from django.urls import include, path

from config.swagger_urls import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('contact/', include('apps.orders.urls')),
    path('services/', include("apps.services.urls")),
    path('auth/', include("apps.authentication.urls")),
]
urlpatterns += swagger_urlpatterns
