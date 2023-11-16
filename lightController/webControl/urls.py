from django.urls import path
from .views import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
    # Add more URL patterns as needed
]