from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import ProfilakkModel 
from .serializers import ProfilakkSerializer

class ProfilakkALLView(ListAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkDetailView(RetrieveAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkUpdateView(UpdateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkCreateView(CreateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkDeleteView(DestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkAllCreateView(ListCreateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkDetailUpdate(RetrieveUpdateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkDetaildeleteView(RetrieveDestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer

class ProfilakkRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer