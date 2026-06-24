from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, CreateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)
from .models import User7Model
from .serializers import User7Serilizer
from rest_framework.permissions import IsAuthenticated
from .permission import IsOwnerPermission


class userAllView(ListAPIView):
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return User7Model.objects.filter(user=self.request.user)


class userDetailView(RetrieveAPIView):
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    def get_queryset(self):
        return User7Model.objects.filter(user=self.request.user)


class userUpdateView(UpdateAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userCreateView(CreateAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userDeleteView(DestroyAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userAllCreateView(ListCreateAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userDetailUpdateView(RetrieveUpdateAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userDetailDeleteView(RetrieveDestroyAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]


class userRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = User7Model.objects.all()
    serializer_class = User7Serilizer
    permission_classes = [IsAuthenticated]
