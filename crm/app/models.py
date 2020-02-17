import jwt
from django.core.mail import send_mail
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
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
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

    name = models.CharField(max_length=255, unique=True, null=False)
    phone = models.CharField(max_length=255, null=True, blank=True)
    ownerFullName = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'TradingSets'

class Manager(models.Model):

    username = models.CharField(max_length=255, unique=True)
    tradingSet = models.OneToOneField('TradingSet', to_field='name', on_delete=models.CASCADE, null=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % (self.username)

    class Meta:
        ordering = ['tradingSet']
        verbose_name_plural = 'Managers'


class User(AbstractBaseUser, PermissionsMixin):

    male = 'male'
    female = 'female'
    GENDER_CHOICES = [(male, "male"), (female, "female")]

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    username = models.CharField(max_length=255, null=False, unique=True)
    email = models.EmailField('email address',db_index=True, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    password = models.CharField(max_length=255, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=1)
    dateOfBirth = models.DateField(default=None, null=True)
    phone = models.CharField(max_length=255, null=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    is_active = models.BooleanField('active', default=True)
    photo = models.ImageField(null=True, blank=True, upload_to='static')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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




class Individual(models.Model):

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Individuals'

    def __str__(self):
        return '%s' % (self.address)


class UserStatus(models.Model):

    status = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'UserStatuses'

    def __str__(self):
        return '%s' % (self.status)


class LegalEntity(models.Model):

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, null=False, primary_key=True, related_name='User')
    description = models.TextField(max_length=255, null=True)
    legalAddress = models.CharField(max_length=255, null=False)
    IIN = models.CharField(max_length=255, null=False)
    bankAccount = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name_plural = 'LegalEntities'

    def __str__(self):
        return '%s, %s' % (self.description , self.legalAddress)


class Driver(models.Model):

    User_id = models.OneToOneField('User', on_delete=models.CASCADE, null=False, primary_key=True)
    autoTechPassPhoto = models.ImageField(null=True, upload_to='static')
    trailerTechPassPhoto = models.ImageField(null=True, upload_to='static')
    autoOwnerPass = models.ImageField(null=True, upload_to='static')
    driverPass = models.ImageField(null=True, upload_to='static')
    driverLicense = models.ImageField(null=True, upload_to='static')
    internationalTransportationLicense = models.ImageField(null=True, upload_to='static')
    insurancePolicy = models.ImageField(null=True, upload_to='static')

    class Meta:
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return '%s' % (self.User_id)
