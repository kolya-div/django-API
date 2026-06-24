from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import FoydaModel 
from .serializers import FoydaSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission   

class FoydaALLView(ListAPIView):
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return FoydaModel.objects.filter(user=self.request.user)

class FoydaDetailView(RetrieveAPIView):
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return FoydaModel.objects.filter(user=self.request.user)

class FoydaUpdateView(UpdateAPIView):
    serializer_class = FoydaSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return FoydaModel.objects.filter(user=self.request.user)

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