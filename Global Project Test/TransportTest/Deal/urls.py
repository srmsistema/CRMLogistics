from django.urls import path
from .views import *

urlpatterns = [
    path('deal/', ListDealView.as_view(), name='deal'),
    path('deal/create/', CreateDealView.as_view(), name = 'create_deal'),
    path('deal/update/<int:pk>', UpdateDealView.as_view(), name = 'update_deal'),
    path('deal/delete/<int:pk>', DeleteDealView.as_view(), name = 'delete_deal'),
    path('type-cargo/create/', CreateTypeCargoView.as_view(), name = 'type_cargo_create'),
    path('type-auto/create/', CreateTypeAutoView.as_view(), name = 'type_auto_create'),
    path('type-loading/create/', CreateTypeLoadingView.as_view(), name = 'type_loading_create'),
    path('units/create/', CreateUnitsView.as_view(), name = 'unit_create'),
    path('weight/create/', CreateWeightView.as_view(), name = 'weight_create'),
    path('volume/create/', CreateVolumeView.as_view(), name = 'volume_create'),
    path('parametres-trailer/create/', CreateParametresTrailerView.as_view(), name = 'parametres_trailer_create'),
    path('location-cargo/create/', CreateLocationCargoView.as_view(), name = 'location_cargo_create'),
    path('deal-status/create/', CreateDealStatusView.as_view(), name = 'deal_status_create'),


]
