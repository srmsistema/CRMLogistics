from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm
from django.contrib.auth.models import Group

from .models import Individual, UserStatus, Driver, TradingSet, Manager, User, Clients
from django.contrib import admin
from .forms import SignupForm
# from Deal.models import Order

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


admin.site.register(Clients)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserStatus)
admin.site.register(Driver)
admin.site.register(Individual)
admin.site.register(TradingSet)
admin.site.register(Manager)
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
# manager_admin_site.register(Order)