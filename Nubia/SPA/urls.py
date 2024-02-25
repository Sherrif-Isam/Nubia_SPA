# SPA/urls.py

from django.urls import path 
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),  # Use an empty string to represent the root URL
]
