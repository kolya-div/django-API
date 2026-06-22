from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import AkkModel 
from .serializers import AkkSerializer
from  rest_framework.permissions import IsAuthenticated

class AkkALLView(ListAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkDetailView(RetrieveAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated] 

class AkkUpdateView(UpdateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkCreateView(CreateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkDeleteView(DestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkAllCreateView(ListCreateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkdetailUpdate(RetrieveUpdateAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkDetaildeleteView(RetrieveDestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]

class AkkRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = AkkModel.objects.all()
    serializer_class = AkkSerializer
    permission_classes = [IsAuthenticated]