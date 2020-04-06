from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from django.contrib.auth.models import Group

from .models import Individual, UserStatus, Driver, TradingSet, Manager, User, Clients
from django.contrib import admin
from .forms import SignupForm
from Deal.models import Order


class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'email', 'is_staff', 'is_active','is_client', 'is_manager', 'is_driver')
    list_filter = ('username', 'email', 'is_staff', 'is_active','is_client', 'is_manager', 'is_driver')
    fieldsets = (
        (None, {'fields': ('username',  'email', 'password','is_client', 'is_manager', 'is_driver')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email','password1','password2', 'is_staff', 'is_active','is_client', 'is_manager', 'is_driver')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'phone', 'dateOfBirth')
    list_filter = ('first_name', 'last_name', )
    search_fields = ('user__username', 'user__email', 'phone', 'first_name', 'last_name')


class DriversAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'date_joined',)
    list_filter = ('first_name', 'last_name', 'user__date_joined', )
    search_fields = ('user__username', 'user__email', 'first_name', 'last_name', 'user__email')

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


admin.site.register(Clients, ClientsAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserStatus)
admin.site.register(Driver, DriversAdmin)
admin.site.register(TradingSet, TradingSetAdmin)
admin.site.register(Manager, ManagerAdmin)
admin.site.register(Individual)
admin.site.unregister(Group)


class ManagerAdminSite(AdminSite):
    site_header = "CRM Logistics Managers"
    site_title = "CRM Logistics Events Managers"
    index_title = "Welcome to CRM Logistics"

manager_admin_site = ManagerAdminSite(name='manager_admin')


class ManagerAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

manager_admin_site.register(TradingSet, ManagerAdmin)
manager_admin_site.register(Order)