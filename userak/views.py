from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import ProfilModel 
from .serializers import ProfilSerializer
from rest_framework.permissions import IsAuthenticated

class ProfilALLView(ListAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilDetailView(RetrieveAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilUpdateView(UpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilCreateView(CreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilDeleteView(DestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilAllCreateView(ListCreateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]

class ProfilDetailUpdate(RetrieveUpdateAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    parser_classes = [IsAuthenticated]

class ProfilDetaildeleteView(RetrieveDestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    parser_classes = [IsAuthenticated]

class ProfilRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = ProfilModel.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]