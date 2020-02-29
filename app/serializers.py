from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password',
                  'gender', 'dateOfBirth', 'phone', 'photo', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'password',
                  'is_staff', 'is_active', 'gender', 'dateOfBirth', 'phone', 'photo']
        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError('A username is required to log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this username and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'username': user.username,
            'token': user.token
        }


class TradingSetSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TradingSet
        fields = ('id', 'name', 'phone', 'ownerFullName', 'description', 'legalAddress', 'IIN', 'bankAccount')


class DriversSerializer(serializers.ModelSerializer):

    User_id = UsersSerializer(required=True)

    class Meta:
        model = Driver
        fields = ('User_id', 'autoTechPassPhoto', 'trailerTechPassPhoto', 'autoOwnerPass', 'driverPass', 'driverLicense',
            'internationalTransportationLicense', 'insurancePolicy')

        def create(self, validated_data):
            user_data = validated_data.pop('User_id')
            user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
            driver, created = Driver.objects.update_or_create(user=user)
            return driver


class IndividualsSerializer(serializers.ModelSerializer):
    
    User_id = UsersSerializer(required=True)
    
    class Meta:
        model = Individual
        fields = ('User_id', 'address')
            
    def create(self, validated_data):
        user_data = validated_data.pop('User_id')
        user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
        individual, created = Individual.objects.update_or_create(user=user)
        return individual


class ManagersSerializer(serializers.ModelSerializer):

    User_id = UsersSerializer(required=True)

    class Meta:
        model = Manager
        fields = ('User_id', 'tradingSet')

    def create(self, validated_data):
        user_data = validated_data.pop('User_id')
        user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
        individual, created = Individual.objects.update_or_create(user=user)
        return individual
