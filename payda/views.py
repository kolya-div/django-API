from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import PaydaModel 
from .serializers import PaydaSerializer
from rest_framework.permissions import IsAuthenticated

class PaydaALLView(ListAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaDetailView(RetrieveAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaUpdateView(UpdateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaCreateView(CreateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaDeleteView(DestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaAllCreateView(ListCreateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydadetailUpdate(RetrieveUpdateAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaDetaildeleteView(RetrieveDestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]

class PaydaRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = PaydaModel.objects.all()
    serializer_class = PaydaSerializer
    permission_classes = [IsAuthenticated]