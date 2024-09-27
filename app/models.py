import datetime

import jwt
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.views.generic import list
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    # exclude = ('',)
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError('Должно быть введено имя пользователя.')
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class TradingSet(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, verbose_name='Название')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='Телефон')
    ownerFullName = models.CharField(max_length=255, null=True, blank=True, verbose_name='ФИО владельца')
    description = models.TextField(max_length=255, null=True, blank=True, verbose_name='Описание')
    legalAddress = models.CharField(max_length=255, null=False, blank=True, verbose_name='Юр. адрес')
    IIN = models.CharField(max_length=255, null=False, blank=True, verbose_name='ИИН')
    bankAccount = models.CharField(max_length=255, null=False, blank=True, verbose_name='Номер счёта')

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['name']
        verbose_name = 'Торговый сет'
        verbose_name_plural = 'Торговые сеты'


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, blank=False, unique=True, default='',
                                verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, blank=True, verbose_name='Почта')
    password = models.CharField(max_length=255, null=False, verbose_name='Пароль')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_client = models.BooleanField(default=False, verbose_name='Клиент')
    is_manager = models.BooleanField(default=False, verbose_name='Менеджер')
    is_driver = models.BooleanField(default=False, verbose_name='Исполнитель')
    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        return self._generate_jwt_token_()

    def _generate_jwt_token_(self):
        user = User.objects.get(id=self.pk)
        refresh = self.get_token(user)
        token = str(refresh.access_token)
        return token

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Manager(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    tradingSet = models.OneToOneField('TradingSet', to_field='name', on_delete=models.CASCADE, null=True,
                                      verbose_name='Торговый сет')

    def __str__(self):
        return '%s' % (self.user)

    class Meta:
        ordering = ['tradingSet']
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'


class Individual(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    address = models.CharField(max_length=255, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Физическое лицо'
        verbose_name_plural = 'Физические лица'

    def __str__(self):
        return '%s' % (self.address)


class UserStatus(models.Model):
    status = models.CharField(max_length=255, verbose_name='Статус')

    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователя'

    def __str__(self):
        return '%s' % (self.status)


class Driver(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    autoTechPassPhoto = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Технический паспорт авто')
    trailerTechPassPhoto = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Технический паспорт прицепа')
    autoOwnerPass = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Паспорт владельца')
    driverPass = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Паспорт водителя')
    driverLicense = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Водительская лицензия')
    internationalTransportationLicense = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static',
                                                           verbose_name='Лицензия на международные перевозки')
    insurancePolicy = models.ImageField(default='static/blank-profile-picture-973460_6404.png', null=False, upload_to='static', verbose_name='Страховой полис')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return '%s' % (self.user)


class Clients(models.Model):
    male = 'male'
    female = 'female'
    GENDER_CHOICES = [(male, "мужской"), (female, "женский")]

    user = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=1, verbose_name='Пол')
    dateOfBirth = models.DateField(default=timezone.now, blank=True, verbose_name='Дата рождения')
    phone = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='Телефон')
    photo = models.ImageField(default='static/blank-profile-picture-973460_6404.png', blank=True, upload_to='static', verbose_name='Фото', null=False)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return '%s' % (self.user)
