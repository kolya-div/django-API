from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import ProfilakkModel 
from .serializers import ProfilakkSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission

class ProfilakkALLView(ListAPIView):
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return ProfilakkModel.objects.filter(user=self.request.user)

class ProfilakkDetailView(RetrieveAPIView):
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return ProfilakkModel.objects.filter(user=self.request.user)

class ProfilakkUpdateView(UpdateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkCreateView(CreateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkDeleteView(DestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkAllCreateView(ListCreateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkDetailUpdate(RetrieveUpdateAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkDetaildeleteView(RetrieveDestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]

class ProfilakkRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = ProfilakkModel.objects.all()
    serializer_class = ProfilakkSerializer
    permission_classes = [IsAuthenticated]