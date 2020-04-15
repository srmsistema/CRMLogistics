from django.contrib import admin
from .models import *


class TypeAutoAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)
    search_fields = ('type',)


class TypeCargoAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)
    search_fields = ('type',)


class TypeLoadingAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)
    search_fields = ('type',)


class TypeLoadingAdmin(admin.ModelAdmin):
    list_display = ('type',)
    list_filter = ('type',)
    search_fields = ('type',)


class LocationCargoAdmin(admin.ModelAdmin):
    list_display = ('address', 'sendingTimeCoordinates')
    list_filter = ('sendingTimeCoordinates',)
    search_fields = ('address',)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        qs = super(LocationCargoAdmin, self).get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            return qs.filter(user__id=request.user.id)
        else:
            return qs


class OrderAdmin(admin.ModelAdmin):

    list_display = ('user', 'driver', 'status', 'fromOrder', 'toOrder')
    list_filter = ('fromOrder', 'toOrder', 'dateLoading', 'dateUnloading',
                   'typeLoading__type', 'typeCargo__type', 'orderStatus', 'user__username')
    search_fields = ('user__username',  'driver__user__username')

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            return qs.filter(user__id=request.user.id)
        else:
            return qs


class StateAwningAdmin(admin.ModelAdmin):

    list_display = ('noHoles', 'noGaps', 'dry', 'noPatches',)

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        qs = super(StateAwningAdmin, self).get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            return qs.filter(user__id=request.user.id)
        else:
            return qs


class VolumeAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_module_permission(self, request):
        return True

    def get_queryset(self, request):
        qs = super(VolumeAdmin, self).get_queryset(request)
        if not request.user.is_superuser and request.user.is_staff:
            return qs.filter(user__id=request.user.id)
        else:
            return qs


#admin.site.register(SubclassHazard)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(TypeAuto, TypeAutoAdmin)
admin.site.register(TypeCargo, TypeCargoAdmin)
admin.site.register(TypeLoading, TypeLoadingAdmin)
admin.site.register(Units)
admin.site.register(StateAwning, StateAwningAdmin)
admin.site.register(LocationCargo, LocationCargoAdmin)
admin.site.register(Order, OrderAdmin)

