from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dailyconsumption', views.DailyConsumptionList, basename='dailyconsumption')

urlpatterns = [
    path('', include(router.urls)),
    # path('<int:user_id>', include(router.urls)),
    path('<int:userid>', include(router.urls)),
]
