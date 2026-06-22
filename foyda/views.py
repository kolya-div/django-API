from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import FoydaModel 
from .serializers import FoydaSerializer
from rest_framework.permissions import IsAuthenticated

class FoydaALLView(ListAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaDetailView(RetrieveAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaUpdateView(UpdateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaCreateView(CreateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaDeleteView(DestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaAllCreateView(ListCreateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydadetailUpdate(RetrieveUpdateAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaDetaildeleteView(RetrieveDestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]

class FoydaRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = FoydaModel.objects.all()
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]