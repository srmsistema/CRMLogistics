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
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=255, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError('An email address is required to log in.')

        if password is None:
            raise serializers.ValidationError('A password is required to log in.')

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password was not found.')

        if not user.is_active:
            raise serializers.ValidationError('This user has been deactivated.')

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token
        }


class TradingSetSerializer(serializers.ModelSerializer):
    serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TradingSet
        fields = ('id', 'name', 'phone', 'ownerFullName')


class LegalEntitySerializer(serializers.ModelSerializer):
    # serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    User_id = UsersSerializer(required=True)

    class Meta:
        model = LegalEntity
        fields = ('User_id', 'description', 'legalAddress', 'IIN', 'bankAccount')

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('User_id')
        user = UsersSerializer.create(UsersSerializer(), validated_data=user_data)
        legalEntity, created = LegalEntity.objects.update_or_create(user=user)
        return legalEntity