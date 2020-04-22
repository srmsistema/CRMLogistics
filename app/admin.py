from django.contrib.admin import AdminSite
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from django.contrib.auth.models import Group

from .models import UserStatus, Driver, TradingSet, Manager, User, Clients
from django.contrib import admin
from .forms import SignupForm
from Deal.models import Order

from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import Group


class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(),
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff','is_client', 'is_driver', 'is_active')
    list_filter = ('username', 'email', 'is_staff','is_client', 'is_driver', 'is_active')
    fieldsets = (
        (None, {'fields': ('username',  'email', 'password','is_client', 'is_driver')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1','password2', 'is_staff', 'is_active','is_client', 'is_driver')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'dateOfBirth')
    list_filter = ('first_name', 'last_name', )
    search_fields = ('user__username', 'user__email', 'phone', 'first_name', 'last_name')


class DriversAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'date_joined', 'phone')
    list_filter = ('first_name', 'last_name', 'user__date_joined', 'auto_type__type',)
    search_fields = ('user__username', 'user__email', 'first_name', 'last_name', 'user__email',
                     'phone', 'address', 'auto_type__type',)

    def date_joined(self, obj):
        return obj.user.date_joined
    date_joined.short_description = 'Дата присоединения'
    date_joined.admin_order_field = 'user__date_joined'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Почта'
    email.admin_order_field = 'user__email'

    def status(self, obj):
        return obj.user.status
    status.short_description = 'Статус'
    status.admin_order_field = 'user__status'


class TradingSetAdmin(admin.ModelAdmin):
    list_display = ('name', 'ownerFullName', 'phone', 'description',)
    list_filter = ('name', 'ownerFullName')
    search_fields = ('name', 'ownerFullName', 'phone')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.is_staff:
            return [f.name for f in self.model._meta.fields]
        return super(TradingSetAdmin, self).get_readonly_fields(
            request, obj=obj
        )


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'date_joined', 'tradingSet',)
    list_filter = ('first_name', 'last_name', 'tradingSet__name')
    search_fields = ('user__username', 'first_name', 'last_name', 'tradingSet__name', 'user__email')


    def date_joined(self, obj):
        return obj.user.date_joined
    date_joined.short_description = 'Дата присоединения'
    date_joined.admin_order_field = 'user__date_joined'

    def email(self, obj):
        return obj.user.email
    email.short_description = 'Почта'
    email.admin_order_field = 'user__email'


admin.site.unregister(Group)
# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserStatus)
admin.site.register(Driver, DriversAdmin)
admin.site.register(TradingSet, TradingSetAdmin)
admin.site.register(Manager, ManagerAdmin)

# admin.site.unregister(Group)


# class ManagerAdminSite(AdminSite):
#     site_header = "CRM Logistics Managers"
#     site_title = "CRM Logistics Events Managers"
#     index_title = "Welcome to CRM Logistics"
#
# manager_admin_site = ManagerAdminSite(name='manager_admin')
#
#
# class ManagerAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False
#
# manager_admin_site.register(Manager, ManagerAdmin)
# manager_admin_site.register(Order)