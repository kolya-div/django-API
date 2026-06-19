from django.urls import path
from .views import (UserALLView, UserDetailView, UserUpdateView, UserCreateView, UserDeleteView,
                    userAllCreateView,UserdetailUpdate,UserDetaildeleteView, UserRetrieveUpdateDestory)

urlpatterns = [
    path('all/', UserALLView.as_view()),
    path('get/<int:pk>', UserDetailView.as_view()),
    path('update/<int:pk>', UserUpdateView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('del<int:pk>', UserDeleteView.as_view()),


    path('allcreate/', userAllCreateView.as_view()),
    path('getupdate/<int:pk>', UserdetailUpdate.as_view()),
    path('getdelete/<int:pk>', UserDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',UserRetrieveUpdateDestory.as_view())
]
