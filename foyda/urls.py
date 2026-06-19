from django.urls import path
from .views import (FoydaALLView, FoydaDetailView, 
                    FoydaUpdateView, FoydaCreateView,  
                    FoydaDeleteView,FoydaAllCreateView,
                    FoydadetailUpdate,FoydaDetaildeleteView, 
                    FoydaRetrieveUpdateDestory)

urlpatterns = [
    path('all/', FoydaALLView.as_view()),
    path('get/<int:pk>', FoydaDetailView.as_view()),
    path('update/<int:pk>', FoydaUpdateView.as_view()),
    path('create/', FoydaCreateView.as_view()),
    path('del<int:pk>', FoydaDeleteView.as_view()),
    path('allcreate/', FoydaAllCreateView.as_view()),
    path('getupdate/<int:pk>', FoydadetailUpdate.as_view()),
    path('getdelete/<int:pk>', FoydaDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',FoydaRetrieveUpdateDestory.as_view())
]
