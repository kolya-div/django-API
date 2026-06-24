from .models import Magluma
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import MaglumaSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission


class MaglumaListAPIView(ListAPIView):
    serializer_class = MaglumaSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Magluma.objects.filter(user=self.request.user)

class MaglumaCreateAPIView(CreateAPIView):
    queryset = Magluma.objects.all()
    serializer_class =  MaglumaSerializer
    permission_classes = (IsAuthenticated,)


class MaglumaDetailAPIView(RetrieveAPIView):
    serializer_class = MaglumaSerializer
    permission_classes = (IsAuthenticated, IsOwnerPermission)

    def get_queryset(self):
        return Magluma.objects.filter(user=self.request.user)