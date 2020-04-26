import csv

from django.contrib import admin
from django.db.models import Max
from django.http import HttpResponse
from django import forms
from django.shortcuts import render

from .models import *


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper


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

    def has_module_permission(self, request):
        return True

    # def get_queryset(self, request):
    #     qs = super(LocationCargoAdmin, self).get_queryset(request)
    #     if not request.user.is_superuser and request.user.is_staff:
    #         return qs.filter(user__id=request.user.id)
    #     else:
    #         return qs


class StateAwningAdmin(admin.ModelAdmin):
    list_display = ('noHoles', 'noGaps', 'dry', 'noPatches',)

    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True


    # def get_queryset(self, request):
    #     qs = super(StateAwningAdmin, self).get_queryset(request)
    #     if not request.user.is_superuser and request.user.is_staff:
    #         return qs.filter(user__id=request.user.id)
    #     else:
    #         return qs


class VolumeAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_module_permission(self, request):
        return True
    #
    # def get_queryset(self, request):
    #     qs = super(VolumeAdmin, self).get_queryset(request)
    #     if not request.user.is_superuser and request.user.is_staff:
    #         return qs.filter(user__id=request.user.id)
    #     else:
    #         return qs


class OrderAdmin(admin.ModelAdmin):
    fields = ('name', 'numberOrderFromClient', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear',
                  'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                  'volume', 'locationCargo', 'user', 'driver', 'orderStatus', 'fromOrder', 'dateOrderConclusion', 'toOrder')
    list_display = ('user', '__str__', 'driver', 'status', 'fromOrder', 'toOrder')
    list_filter = (('driver__user__username', custom_titled_filter('Имя пользователя водителя')), 'fromOrder', 'toOrder', 'dateLoading', 'dateUnloading',
                   'typeLoading__type', 'typeCargo__type', 'orderStatus',
                   ('user__username', custom_titled_filter('Имя пользователя клиента') ))
    search_fields = ('user__username',  'driver__user__username')
    readonly_fields = ('numberOrderFromClient', 'fromOrder', 'dateOrderConclusion', 'toOrder', 'dateLoading',
                       'dateUnloading', 'driver', 'orderStatus', 'user')

    def lookup_allowed(self, key, value):
        if key in ('driver__user__username'):
            return True
        return super(OrderAdmin, self).lookup_allowed(key, value)

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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        orders_qs = Order.objects.filter(user=request.user)
        if orders_qs:
            num = orders_qs.aggregate(Max('numberOrderFromClient'))
            if num['numberOrderFromClient__max'] is None:
                num['numberOrderFromClient__max'] = 0
            num['numberOrderFromClient__max'] += 1
            obj.numberOrderFromClient = num['numberOrderFromClient__max']
        obj.save()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            if request.user.is_superuser:
                return ()
            if request.user.is_staff:
                return ['name', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear', 'companyProfit',
                      'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                      'volume', 'locationCargo', 'user', 'driver', 'orderStatus', 'fromOrder', 'dateOrderConclusion',
                      'toOrder', 'weightMeasurementUnit', 'numberOrderFromClient']
        return super(OrderAdmin, self).get_readonly_fields(request, obj=obj)

    def get_fields(self, request, obj=None):
        fields = list(super(OrderAdmin, self).get_fields(request, obj))
        exclude_set = set()
        if not obj:  # obj will be None on the add page, and something on change pages
            exclude_set.add('dateLoading')
            exclude_set.add('dateUnloading')
            exclude_set.add('user')
            exclude_set.add('driver')
            exclude_set.add('orderStatus')
            exclude_set.add('fromOrder')
            exclude_set.add('dateOrderConclusion')
            exclude_set.add('toOrder')
            exclude_set.add('numberOrderFromClient')
        return [f for f in fields if f not in exclude_set]


#admin.site.register(SubclassHazard)
admin.site.register(Volume, VolumeAdmin)
admin.site.register(TypeAuto, TypeAutoAdmin)
admin.site.register(TypeCargo, TypeCargoAdmin)
admin.site.register(TypeLoading, TypeLoadingAdmin)
admin.site.register(Units)
admin.site.register(StateAwning, StateAwningAdmin)
admin.site.register(LocationCargo, LocationCargoAdmin)
admin.site.register(Order, OrderAdmin)

