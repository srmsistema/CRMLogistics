from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from django.contrib.auth.models import Group

from .models import Individual, UserStatus, Driver, LegalEntity, TradingSet, Manager, User
from django.contrib import admin
from .forms import SignupForm


class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'gender',
                           'dateOfBirth', 'phone', 'photo', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name','email', 'gender',
                           'dateOfBirth', 'phone', 'photo', 'password1',
                       'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserStatus)
admin.site.register(Driver)
admin.site.register(Individual)
admin.site.register(LegalEntity)
admin.site.register(TradingSet)
admin.site.register(Manager)
admin.site.unregister(Group)
