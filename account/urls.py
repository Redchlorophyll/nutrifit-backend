from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserDetail, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>', include(router.urls)),
]
