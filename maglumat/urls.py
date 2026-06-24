from django.urls import path
from .views import MaglumaListAPIView, MaglumaCreateAPIView, MaglumaDetailAPIView

urlpatterns = [
    path('all/', MaglumaListAPIView.as_view()),
    path('create/', MaglumaCreateAPIView.as_view()),
    path('get/<int:pk>', MaglumaDetailAPIView.as_view())
]