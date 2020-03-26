from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

# class RegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         max_length=128,
#         min_length=8,
#         write_only=True,
#         style={'input_type': 'password'}
#     )
#
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password','token')
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        style={'input_type': 'password'}
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','token')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','is_staff','is_active',
                  'is_client', 'is_manager', 'is_driver', 'status', 'token')

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
    password = serializers.CharField(max_length=255, write_only=True, style={'input_type': 'password'})
    token = serializers.CharField(max_length=255, read_only=True)
    status = serializers.CharField(max_length=255, read_only=True)

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
            'email': user.email,
            'token': user.token,
            'status': user.status
        }


class TradingSetSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TradingSet
        fields = ('id', 'name', 'phone', 'ownerFullName', 'description', 'legalAddress', 'IIN', 'bankAccount')


class DriversSerializer(serializers.ModelSerializer):

    user = UsersSerializer(required=True)

    class Meta:
        model = Driver
        fields = ('user', 'autoTechPassPhoto', 'trailerTechPassPhoto', 'autoOwnerPass', 'driverPass', 'driverLicense',
            'internationalTransportationLicense', 'insurancePolicy')

        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
            driver, created = Driver.objects.update_or_create(user=user)
            return driver


class IndividualsSerializer(serializers.ModelSerializer):
    
    user = UsersSerializer(required=True)
    
    class Meta:
        model = Individual
        fields = ('user', 'address')
            
    def create(self, validated_data):
        user_data = validated_data.pop('User_id')
        user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
        individual, created = Individual.objects.update_or_create(user=user)
        return individual


class ManagersSerializer(serializers.ModelSerializer):

    user = UsersSerializer(required=True)

    class Meta:
        model = Manager
        fields = ('user', 'tradingSet')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
        individual, created = Individual.objects.update_or_create(user=user)
        return individual

class ClientSerializer(serializers.ModelSerializer):

    user = UsersSerializer(required=True)

    class Meta:
        model =  Clients
        fields = ('user','first_name', 'last_name', 'gender', 'dateOfBirth', 'phone', 'photo')


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password','token')

        read_only_fields = ('id', 'token','is_staff','is_active',
                            'is_client', 'is_manager', 'is_driver', 'status', )

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ClientRegistrationSerializer(serializers.ModelSerializer):

    user = UsersSerializer(required=True)

    class Meta:
        model =  Clients
        fields = ('user','first_name', 'last_name', 'gender', 'dateOfBirth', 'phone', 'photo')
        read_only_fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        client = Clients.objects.create(user=user, **validated_data)
        user.is_client = True
        user.save()
        client.save()
        return client
