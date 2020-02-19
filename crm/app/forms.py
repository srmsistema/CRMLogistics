
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'gender', 'dateOfBirth', 'phone', 'photo')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'gender', 'dateOfBirth', 'phone', 'photo')