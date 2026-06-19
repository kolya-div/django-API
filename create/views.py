from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import CreateModel 
from .serializers import CreateSerializer

class CreateALLView(ListAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateDetailView(RetrieveAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateUpdateView(UpdateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateCreateView(CreateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateDeleteView(DestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateAllCreateView(ListCreateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateDetailUpdate(RetrieveUpdateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateDetaildeleteView(RetrieveDestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer

class CreateRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer