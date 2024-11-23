from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserLoginSerializer, UpdateMoney, UpdateHero
from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login
from user.models import User
import json


@api_view(['POST'])
def UserRegisterView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_202_ACCEPTED)
        print(serializer.errors)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updateMoney(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateMoney(instance=user, data=data)

        if serializer.is_valid():
            update_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def updateHero(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode())
        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UpdateHero(instance=user, data=data)

        if serializer.is_valid():
            update_user = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

api_view(['Get'])
def getData(request):
    if request.method == 'GET':
        username = request.GET.get('username', None)
        try:
            user = User.objects.get(username=username)
            responseData = {
                'money': user.money,
                'maximumMoney': user.maximumMoney,
                'heroStrength': user.heroStrength,
                'heroSpeed': user.heroSpeed,
                'heroDurability': user.heroDurability,
            }
            print(responseData)
            return JsonResponse(responseData)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
