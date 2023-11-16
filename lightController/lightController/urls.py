from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard.views import dashboard
from api import urls

admin.autodiscover()


# add patterns for dashboard and api (router)
urlpatterns = [
    path('', include('dashboard.urls')),
    path('api', include('api.urls'))
]
