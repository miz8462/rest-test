from django.urls import path
from .views import TopView, WeatherDetailView


urlpatterns = [
    path('top/', TopView.as_view()),
    path('detail/<int:pk>', WeatherDetailView.as_view()),
]
