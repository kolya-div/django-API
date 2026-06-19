from django.urls import path
from .views import (CreateALLView, CreateDetailView, 
                    CreateUpdateView, CreateCreateView,  
                    CreateDeleteView,CreateAllCreateView,
                    CreateDetailUpdate,CreateDetaildeleteView, 
                    CreateRetrieveUpdateDestory)

urlpatterns = [
    path('all/', CreateALLView.as_view()),
    path('get/<int:pk>', CreateDetailView.as_view()),
    path('update/<int:pk>', CreateUpdateView.as_view()),
    path('create/', CreateCreateView.as_view()),
    path('del<int:pk>', CreateDeleteView.as_view()),
    path('allcreate/', CreateAllCreateView.as_view()),
    path('getupdate/<int:pk>', CreateDetailUpdate.as_view()),
    path('getdelete/<int:pk>', CreateDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',CreateRetrieveUpdateDestory.as_view())
]
