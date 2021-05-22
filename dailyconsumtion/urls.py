from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('dailyconsumption', views.DailyConsumptionList, basename='dailyconsumption')

urlpatterns = [
    path('', include(router.urls)),
    path('uploadimage/', views.CapturedImage.as_view()),
    path('uploadimage/<int:imageid>/', views.getImage.as_view()),
    # path('<int:user_id>', include(router.urls)),
    path('journey/<int:userid>/', views.FoodJourney.as_view()),
    path('journey/<int:userid>/<str:date>/', views.FoodName.as_view()),
    path('<int:userid>/', include(router.urls)),
]
