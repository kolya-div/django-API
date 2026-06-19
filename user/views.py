from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import UserModel 
from .serializers import UserSerializer





class UserALLView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class userAllCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserdetailUpdate(RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserDetaildeleteView(RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer