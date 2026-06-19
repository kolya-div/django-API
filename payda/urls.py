from django.urls import path
from .views import (PaydaALLView, PaydaDetailView, PaydaUpdateView, PaydaCreateView, PaydaDeleteView,
                    PaydaAllCreateView,PaydadetailUpdate,PaydaDetaildeleteView, PaydaRetrieveUpdateDestory)

urlpatterns = [
    path('all/', PaydaALLView.as_view()),
    path('get/<int:pk>', PaydaDetailView.as_view()),
    path('update/<int:pk>', PaydaUpdateView.as_view()),
    path('create/', PaydaCreateView.as_view()),
    path('del<int:pk>', PaydaDeleteView.as_view()),


    path('allcreate/', PaydaAllCreateView.as_view()),
    path('getupdate/<int:pk>', PaydadetailUpdate.as_view()),
    path('getdelete/<int:pk>', PaydaDetaildeleteView.as_view()),
    path('getupdel/<int:pk>',PaydaRetrieveUpdateDestory.as_view())
]
