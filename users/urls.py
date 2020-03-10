"""Define url patterns for userss app"""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', include('django.contrib.auth.urls')),
]