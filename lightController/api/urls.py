from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

admin.autodiscover()

# Create routers for mode and state viewsets
router = DefaultRouter() 
router.register(r'mode', views.ModeViewSet) 
router.register(r'state', views.StateViewSet) 

# add patterns for dashboard and api (router)
urlpatterns = [
    path('/', include(router.urls)),
]
