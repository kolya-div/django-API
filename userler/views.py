from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import AkkModel 
from .serializers import AkkSerializer

class AkkALLView(ListAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkDetailView(RetrieveAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkUpdateView(UpdateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkCreateView(CreateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkDeleteView(DestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkAllCreateView(ListCreateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkdetailUpdate(RetrieveUpdateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkDetaildeleteView(RetrieveDestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer

class AkkRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer