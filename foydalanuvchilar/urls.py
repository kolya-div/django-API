from django.urls import path
from .views import (FoydalanuchilarALLView, FoydalanuchilarDetailView, 
                    FoydalanuchilarUpdateView, FoydalanuchilarCreateView,  
                    FoydalanuchilarDeleteView,FoydalanuchilarAllCreateView,
                    FoydalanuchilarDetailUpdate,FoydalanuchilarDetaildeleteView, 
                    FoydalanuchilarRetrieveUpdateDestory)

urlpatterns = [
    path('all/', FoydalanuchilarALLView.as_view()),
    path('get/<int:pk>', FoydalanuchilarDetailView.as_view()),
    path('update/<int:pk>', FoydalanuchilarUpdateView.as_view()),
    path('create/', FoydalanuchilarCreateView.as_view()),
    path('del<int:pk>', FoydalanuchilarDeleteView.as_view()),
    path('allcreate/', FoydalanuchilarAllCreateView.as_view()),
    path('getupdate/<int:pk>', FoydalanuchilarDetailUpdate.as_view()),
    path('getdelete/<int:pk>', FoydalanuchilarDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',FoydalanuchilarRetrieveUpdateDestory.as_view())
]
