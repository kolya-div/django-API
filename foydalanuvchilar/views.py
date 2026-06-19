from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import FoydalanuchilarModel 
from .serializers import FoydalanuchilarSerializer

class FoydalanuchilarALLView(ListAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarDetailView(RetrieveAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarUpdateView(UpdateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarCreateView(CreateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarDeleteView(DestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarAllCreateView(ListCreateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarDetailUpdate(RetrieveUpdateAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarDetaildeleteView(RetrieveDestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer

class FoydalanuchilarRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = FoydalanuchilarModel.objects.all()
    serializer_class = FoydalanuchilarSerializer