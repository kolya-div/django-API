from django.urls import path
from .views import (userAllView, userDetailView, userUpdateView,
                    CreateAPIView, DestroyAPIView, userAllCreateView,
                    userDetailUpdateView, userDetailDeleteView, userRetrieveUpdateDestroyView)

urlpatterns = [
    path('all/', userAllView.as_view()),
    path('get/<int:pk>', userDetailView.as_view()),
    path('update/<int:pk>', userUpdateView.as_view()),
    path('create/<int:pk>', CreateAPIView.as_view()),
    path('delete/<int:pk>', DestroyAPIView.as_view()),
    path('dilshat2/<int:pk>', userAllCreateView.as_view()),
    path('ilxam/<int:pk>', userDetailUpdateView.as_view()),
    path('kolya/<int:pk>', userDetailDeleteView.as_view()),
    path('RetrieveUpdateDestroy/<int:pk>', userRetrieveUpdateDestroyView.as_view()),
]
