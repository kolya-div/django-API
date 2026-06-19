from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import ProfilModel 
from .serializers import ProfilSerializer

class ProfilALLView(ListAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilDetailView(RetrieveAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilUpdateView(UpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilCreateView(CreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilDeleteView(DestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilAllCreateView(ListCreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilDetailUpdate(RetrieveUpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilDetaildeleteView(RetrieveDestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer

class ProfilRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer