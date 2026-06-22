from django.urls import path
from .views import (AkkALLView, AkkDetailView, AkkUpdateView, AkkCreateView, AkkDeleteView,
                    AkkAllCreateView,AkkdetailUpdate,AkkDetaildeleteView, AkkRetrieveUpdateDestory)

urlpatterns = [
    path('all/', AkkALLView.as_view()),
    path('get/<int:pk>', AkkDetailView.as_view()),
    path('update/<int:pk>', AkkUpdateView.as_view()),
    path('create/', AkkCreateView.as_view()),
    path('del<int:pk>', AkkDeleteView.as_view()),
    path('allcreate/', AkkAllCreateView.as_view()),
    path('getupdate/<int:pk>', AkkdetailUpdate.as_view()),
    path('getdelete/<int:pk>', AkkDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',AkkRetrieveUpdateDestory.as_view())
]
