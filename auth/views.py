from django.contrib.auth.models import User
from auth.serializers import RegistrationSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from auth.serializers import BretailerzTokenObtainPairSerializer


class BretailerzTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny, )
    serializer_class = BretailerzTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer
