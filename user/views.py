from rest_framework.generics import (ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView,
                                    ListCreateAPIView,RetrieveUpdateAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView)
from .models import UserModel 
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission




class UserALLView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return UserModel.objects.filter(user=self.request.user)

class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return UserModel.objects.filter(user=self.request.user)

class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class userAllCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserdetailUpdate(RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetaildeleteView(RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRetrieveUpdateDestory(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
