from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from webControl import views 

admin.autodiscover()

# Create routers for mode and state viewsets
router = DefaultRouter() 
router.register(r'mode', views.ModeViewSet) 
router.register(r'state', views.StateViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
#    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), 
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^home/', 'webControl.views.home'),
#