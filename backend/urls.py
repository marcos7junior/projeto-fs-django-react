
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
