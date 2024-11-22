from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer, UserTokenSerializer
from django.contrib.auth import get_user_model

# Регистрация
class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

# Вход
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token = RefreshToken.for_user(user)
            return Response({
                'access_token': str(token.access_token),
                'refresh_token': str(token),
                'user': UserTokenSerializer(user).data
            })
        return Response({'error': 'Invalid credentials'}, status=400)

# Получение информации о текущем пользователе
class CurrentUserView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserTokenSerializer

    def get_object(self):
        return self.request.user
