from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import FoydalanuchilarModel 
from .serializers import FoydalanuchilarSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission

class FoydalanuchilarALLView(ListAPIView):
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return FoydalanuchilarModel.objects.filter(user=self.request.user)

class FoydalanuchilarDetailView(RetrieveAPIView):
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]

    def get_queryset(self):
        return FoydalanuchilarModel.objects.filter(user=self.request.user)

class FoydalanuchilarUpdateView(UpdateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarCreateView(CreateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarDeleteView(DestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarAllCreateView(ListCreateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarDetailUpdate(RetrieveUpdateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarDetaildeleteView(RetrieveDestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]

class FoydalanuchilarRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer
    permission_classes = [IsAuthenticated]