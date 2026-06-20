from django.urls import path
from .views import (ProfilakkALLView, ProfilakkDetailView, 
                    ProfilakkUpdateView, ProfilakkCreateView,  
                    ProfilakkDeleteView,ProfilakkAllCreateView,
                    ProfilakkDetailUpdate,ProfilakkDetaildeleteView, 
                    ProfilakkRetrieveUpdateDestory)

urlpatterns = [
    path('all/', ProfilakkALLView.as_view()),
    path('get/<int:pk>', ProfilakkDetailView.as_view()),
    path('update/<int:pk>', ProfilakkUpdateView.as_view()),
    path('create/', ProfilakkCreateView.as_view()),
    path('del<int:pk>', ProfilakkDeleteView.as_view()),
    path('allcreate/', ProfilakkAllCreateView.as_view()),
    path('getupdate/<int:pk>', ProfilakkDetailUpdate.as_view()),
    path('getdelete/<int:pk>', ProfilakkDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',ProfilakkRetrieveUpdateDestory.as_view())
]