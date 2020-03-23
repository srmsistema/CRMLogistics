from django.urls import path
from .views import *

urlpatterns = [
    path('order/', ListOrderAPIView.as_view(), name='order'),
    path('order/<int:pk>', UpdateOrderAPIView.as_view(), name = 'detail_order'),
    path('order/create/', CreateOrderAPIView.as_view(), name = 'create_order'),
    path('order/update/<int:pk>', UpdateOrderAPIView.as_view(), name = 'update_order'),
    path('order/delete/<int:pk>', DeleteOrderAPIView.as_view(), name = 'delete_order'),
    path('type-cargo/create/',  CreateTypeCargoAPIView.as_view(), name = 'type_cargo_create'),
    path('type-cargo/update/<int:pk>', UpdateTypeCargoAPIView.as_view(), name = 'type_cargo_update'),
    path('type-auto/create/', CreateTypeAutoAPIView.as_view(), name = 'type_auto_create'),
    path('type-auto/update/<int:pk>', UpdateTypeAutoAPIView.as_view(), name = 'type_auto_update'),
    path('type-loading/create/', CreateTypeLoadingAPIView.as_view(), name = 'type_loading_create'),
    path('type-loading/update/', UpdateTypeLoadingAPIView.as_view(), name = 'type_loading_update'),
    path('units/create/', CreateUnitsAPIView.as_view(), name = 'unit_create'),
    path('units/update/<int:pk>', UpdateUnitsAPIView.as_view(), name = 'unit_update'),
    # path('weight/create/', CreateWeightView.as_view(), name = 'weight_create'),
    path('weight/update/<int:pk>', UpdateUnitsAPIView.as_view(), name='weight_update'),
    path('volume/create/', CreateVolumeAPIView.as_view(), name = 'volume_create'),
    path('volume/update/<int:pk>', UpdateVolumeAPIView.as_view(), name='volume_update'),
    path('parametres-trailer/create/', CreateParametresTrailerAPIView.as_view(), name = 'parametres_trailer_create'),
    path('parametres-trailer/update/<int:pk>', UpdateParametresTrailerAPIView.as_view(), name='parametres_trailer_update'),
    path('location-cargo/create/', CreateLocationCargoAPIView.as_view(), name = 'location_cargo_create'),
    path('location-cargo/update/', UpdateLocationCargoAPIView.as_view(), name = 'location_cargo_update'),
    # path('deal-status/create/', CreateDealStatusView.as_view(), name = 'deal_status_create'),
    # path('deal-status/update/<int:pk>', UpdateDealStatusView.as_view(), name = 'deal_status_update'),
]
