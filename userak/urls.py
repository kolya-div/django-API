from django.urls import path
from .views import (ProfilALLView, ProfilDetailView, 
                    ProfilUpdateView, ProfilCreateView,  
                    ProfilDeleteView,ProfilAllCreateView,
                    ProfilDetailUpdate,ProfilDetaildeleteView, 
                    ProfilRetrieveUpdateDestory)

urlpatterns = [
    path('all/', ProfilALLView.as_view()),
    path('get/<int:pk>', ProfilDetailView.as_view()),
    path('update/<int:pk>', ProfilUpdateView.as_view()),
    path('create/', ProfilCreateView.as_view()),
    path('del<int:pk>', ProfilDeleteView.as_view()),
    path('allcreate/', ProfilAllCreateView.as_view()),
    path('getupdate/<int:pk>', ProfilDetailUpdate.as_view()),
    path('getdelete/<int:pk>', ProfilDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',ProfilRetrieveUpdateDestory.as_view())
]