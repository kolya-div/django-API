from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import PaydaModel 
from .serializers import PaydaSerializer

class PaydaALLView(ListAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaDetailView(RetrieveAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaUpdateView(UpdateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaCreateView(CreateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaDeleteView(DestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaAllCreateView(ListCreateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydadetailUpdate(RetrieveUpdateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaDetaildeleteView(RetrieveDestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer

class PaydaRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer