import jwt
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
import datetime
from datetime import datetime, timedelta
from django.conf import settings


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    #exclude = ('',)
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not username:
            raise ValueError(_('Должно быть введено имя пользователя.'))
        if email:
            email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,username, email, password, **extra_fields):
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

    male = 'male'
    female = 'female'
    GENDER_CHOICES = [(male, "мужской"), (female, "женский")]

    is_admin = models.BooleanField(default=False, verbose_name='Администратор')
    is_staff = models.BooleanField(default=False, verbose_name='Персонал')
    username = models.CharField(db_index=True, max_length=255, blank=False, unique=True, default='', verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, blank=True, verbose_name='Почта')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    password = models.CharField(max_length=255, null=False, verbose_name='Пароль')
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=1, verbose_name='Пол')
    dateOfBirth = models.DateField(default=None, null=True, blank=True, verbose_name='Дата рождения')
    phone = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name='Телефон')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    photo = models.ImageField(null=True, blank=True, upload_to='static', verbose_name='Фото')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())  # CHANGE HERE
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Manager(models.Model):

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
    tradingSet = models.OneToOneField('TradingSet', to_field='name', on_delete=models.CASCADE, null=True, verbose_name='Торговый сет')

    def __str__(self):
        return '%s' % (self.User_id)

    class Meta:
        ordering = ['tradingSet']
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'



class Individual(models.Model):

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True, verbose_name='Пользователь')
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

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, null=False, primary_key=True, verbose_name='Пользователь')
    autoTechPassPhoto = models.ImageField(null=True, upload_to='static', verbose_name='Технический паспорт авто')
    trailerTechPassPhoto = models.ImageField(null=True, upload_to='static', verbose_name='Технический паспорт прицепа')
    autoOwnerPass = models.ImageField(null=True, upload_to='static', verbose_name='Паспорт владельца')
    driverPass = models.ImageField(null=True, upload_to='static', verbose_name='Паспорт водителя')
    driverLicense = models.ImageField(null=True, upload_to='static', verbose_name='Водительская лицензия')
    internationalTransportationLicense = models.ImageField(null=True, upload_to='static', verbose_name='Лицензия на международные перевозки')
    insurancePolicy = models.ImageField(null=True, upload_to='static', verbose_name='Страховой полис')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return '%s' % (self.User_id)
