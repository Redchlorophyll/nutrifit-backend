from django.urls import path
from . import views

app_name='gmailauth'
urlpatterns = [
    path('', views.DummyView.as_view()),
    path('login/', views.GoogleView.as_view()),
]
