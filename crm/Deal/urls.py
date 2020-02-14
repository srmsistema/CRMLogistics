from django.urls import path
from .views import *

urlpatterns = [
    path('deal/', ListDealView.as_view(), name='deal'),
    path('deal/create/', CreateDealView.as_view(), name = 'create_deal'),
    path('deal/update/<int:pk>', UpdateDealView.as_view(), name = 'update_deal'),
    path('deal/delete/<int:pk>', DeleteDealView.as_view(), name = 'delete_deal'),
    path('type-cargo/create/',  CreateTypeCargoView.as_view(), name = 'type_cargo_create'),
    path('type-cargo/update/<int:pk>', UpdateTypeCargoView.as_view(), name = 'type_cargo_update'),
    path('type-auto/create/', CreateTypeAutoView.as_view(), name = 'type_auto_create'),
    path('type-auto/update/<int:pk>', UpdateTypeAutoView.as_view(), name = 'type_auto_update'),
    path('type-loading/create/', CreateTypeLoadingView.as_view(), name = 'type_loading_create'),
    path('type-loading/update/', UpdateTypeLoadingView.as_view(), name = 'type_loading_update'),
    path('units/create/', CreateUnitsView.as_view(), name = 'unit_create'),
    path('units/update/<int:pk>', UpdateUnitsView.as_view(), name = 'unit_update'),
    path('weight/create/', CreateWeightView.as_view(), name = 'weight_create'),
    path('weight/update/<int:pk>', UpdateUnitsView.as_view(), name='weight_update'),
    path('volume/create/', CreateVolumeView.as_view(), name = 'volume_create'),
    path('volume/update/<int:pk>', UpdateVolumeView.as_view(), name='volume_update'),
    path('parametres-trailer/create/', CreateParametresTrailerView.as_view(), name = 'parametres_trailer_create'),
    path('parametres-trailer/update/<int:pk>', UpdateParametresTrailerView.as_view(), name='parametres_trailer_update'),
    path('location-cargo/create/', CreateLocationCargoView.as_view(), name = 'location_cargo_create'),
    path('location-cargo/update/', UpdateLocationCargoView.as_view(), name = 'location_cargo_update'),
    path('deal-status/create/', CreateDealStatusView.as_view(), name = 'deal_status_create'),
    path('deal-status/update/<int:pk>', UpdateDealStatusView.as_view(), name = 'deal_status_update'),


]
