from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import FoydaModel 
from .serializers import FoydaSerializer

class FoydaALLView(ListAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaDetailView(RetrieveAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaUpdateView(UpdateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaCreateView(CreateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaDeleteView(DestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaAllCreateView(ListCreateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydadetailUpdate(RetrieveUpdateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaDetaildeleteView(RetrieveDestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer

class FoydaRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer