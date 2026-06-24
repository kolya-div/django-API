from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import CreateModel 
from .serializers import CreateSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission

class CreateALLView(ListAPIView):
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return CreateModel.objects.filter(user=self.request.user)

class CreateDetailView(RetrieveAPIView):
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return CreateModel.objects.filter(user=self.request.user)

class CreateUpdateView(UpdateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateCreateView(CreateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateDeleteView(DestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateAllCreateView(ListCreateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateDetailUpdate(RetrieveUpdateAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateDetaildeleteView(RetrieveDestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]

class CreateRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = CreateModel.objects.all()
    serializer_class = CreateSerializer
    permission_classes = [IsAuthenticated]