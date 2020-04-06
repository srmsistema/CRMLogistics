from django.contrib import admin
from .models import *
from django import forms


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


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'driver', 'status', 'fromOrder', 'toOrder')
    list_filter = ('fromOrder', 'toOrder', 'dateLoading', 'dateUnloading',
                   'typeLoading__type', 'typeCargo__type', 'orderStatus')
    search_fields = ('user__username', 'driver__username', )


#admin.site.register(SubclassHazard)
admin.site.register(Volume)
admin.site.register(TypeAuto, TypeAutoAdmin)
admin.site.register(TypeCargo, TypeCargoAdmin)
admin.site.register(TypeLoading, TypeLoadingAdmin)
admin.site.register(Units)
admin.site.register(LocationCargo, LocationCargoAdmin)
admin.site.register(Order, OrderAdmin)

