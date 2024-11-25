from django.contrib.auth import get_user_model
from rest_framework import serializers
from user.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user


# class UpdateMoney(serializers.ModelSerializer):
#     money = serializers.IntegerField(write_only=True)
#     maximumMoney = serializers.IntegerField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['username', 'money', 'maximumMoney']
#
#     def update(self, instance, validated_data):
#         instance.money = validated_data.get('money', instance.money)
#         instance.maximumMoney = validated_data.get('maximumMoney', instance.maximumMoney)
#         instance.save()
#         return instance
#
#
# class UpdateHero(serializers.ModelSerializer):
#     heroStrength = serializers.IntegerField(default=1)
#     heroSpeed = serializers.IntegerField(default=1)
#     heroDurability = serializers.IntegerField(default=1)
#
#     class Meta:
#         model = User
#         fields = ['username', 'heroStrength', 'heroSpeed', 'heroDurability']
#
#     def update(self, instance, validated_data):
#         instance.heroStrength = validated_data.get('heroStrength', instance.heroStrength)
#         instance.heroSpeed = validated_data.get('heroSpeed', instance.heroSpeed)
#         instance.heroDurability = validated_data.get('heroDurability', instance.heroDurability)
#         instance.save()
#         return instance

class UpdateData(serializers.ModelSerializer):
    money = serializers.IntegerField(write_only=True)
    maximumMoney = serializers.IntegerField(write_only=True)
    heroStrength = serializers.IntegerField(default=1)
    heroSpeed = serializers.IntegerField(default=1)
    heroDurability = serializers.IntegerField(default=1)
    chosenLeague = serializers.IntegerField(default=1)

    class Meta:
        model = User
        fields = ['username', 'money', 'maximumMoney', 'heroStrength', 'heroSpeed', 'heroDurability', 'chosenLeague']

    def update(self, instance, validated_data):
        instance.money = validated_data.get('money', instance.money)
        instance.maximumMoney = validated_data.get('maximumMoney', instance.maximumMoney)
        instance.heroStrength = validated_data.get('heroStrength', instance.heroStrength)
        instance.heroSpeed = validated_data.get('heroSpeed', instance.heroSpeed)
        instance.heroDurability = validated_data.get('heroDurability', instance.heroDurability)
        instance.chosenLeague = validated_data.get('chosenLeague', instance.chosenLeague)
        instance.save()
        return instance
