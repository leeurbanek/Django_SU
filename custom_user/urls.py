"""user URL Configuration
"""
from django.urls import include, path

from . import views


urlpatterns = [
    path('profile/', views.ProfilePageView.as_view(), name='profile'),
    path('', include('allauth.urls')),
]
