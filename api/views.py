from django.contrib.auth import get_user_model  # If used custom user model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers.userserializer import RegisterUserSerializer, UserSerializer


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterUserSerializer


class UsersView(ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
