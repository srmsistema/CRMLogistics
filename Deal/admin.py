from django.contrib import admin
from .models import *
from django import forms

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         exclude = ('numberOrderFromClient', 'priceClient', 'companyProfit',
#                    'fromOrder', 'toOrder', 'dateLoading', 'dateUnloading', 'owner')
#
# class OrderAdmin(admin.ModelAdmin):
#     # exclude = ('fromOrder', 'toOrder', 'companyProfit')
#     form = OrderForm

#admin.site.register(SubclassHazard)
admin.site.register(Volume)
#admin.site.register(Weight)
admin.site.register(TypeAuto)
admin.site.register(TypeCargo)
# admin.site.register(TypeLoading)
admin.site.register(Units)
# admin.site.register(ParametresTrailer)
# admin.site.register(LocationCoordinatesStatus)
admin.site.register(LocationCargo)
# admin.site.register(DealStatus)
# admin.site.register(Order, OrderAdmin)
admin.site.register(Order)

