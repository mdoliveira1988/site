from django.urls import path

from SaibaMais import views
from inicio.views import index, my_api_view

urlpatterns = [
    path('', index),
    path('my-api/', my_api_view, name='my_api'),
]