from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from GeoApp.views import BuildingViewSet

router = DefaultRouter()
router.register(r'buildings', BuildingViewSet, basename='building')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
