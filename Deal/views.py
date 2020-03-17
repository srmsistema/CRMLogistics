from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework import permissions
from .permissions import IsManager, IsClient
from app.models import Clients


class ListOrderAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAdminUser | IsClient | IsManager]

    def get_queryset(self):
        if self.request.user.is_staff and self.request.user:
            return Clients.objects.all()
        elif self.request.user.is_client and self.request.user:
            return Clients.objects.filter(user=self.request.user)
        elif self.request.user.is_manager and self.request.user:
            return Clients.objects.filter(user=self.request.user)


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser | IsManager | IsClient]


class UpdateOrderAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class DeleteOrderAPIView(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateTypeCargoAPIView(ListCreateAPIView):
    queryset = TypeCargo.objects.all()
    serializer_class = TypeCargoSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateTypeCargoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TypeCargo.objects.all()
    serializer_class = TypeCargoSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateTypeAutoAPIView(ListCreateAPIView):
    queryset = TypeAuto.objects.all()
    serializer_class = TypeAutoSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateTypeAutoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TypeAuto.objects.all()
    serializer_class = TypeAutoSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateTypeLoadingAPIView(ListCreateAPIView):
    queryset = TypeLoading.objects.all()
    serializer_class = TypeLoadingSerializer
    permission_classes = (permissions.IsAdminUser)


class UpdateTypeLoadingAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TypeLoading.objects.all()
    serializer_class = TypeLoadingSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateUnitsAPIView(ListCreateAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateUnitsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    permission_classes = [permissions.IsAdminUser]


# class CreateWeightView(ListCreateAPIView):
#     queryset = Weight.objects.all()
#     serializer_class = WeightSerializer
#     # permission_classes = (permissions.IsAdminUser)


# class UpdateWeightView(RetrieveUpdateDestroyAPIView):
#     queryset = Weight.objects.all()
#     serializer_class = WeightSerializer
#     # permission_classes = (permissions.IsAdminUser)


class CreateVolumeAPIView(ListCreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateVolumeAPIView(RetrieveDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateParametresTrailerAPIView(ListCreateAPIView):
    queryset = ParametresTrailer.objects.all()
    serializer_class = ParametresTrailerSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateParametresTrailerAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ParametresTrailer.objects.all()
    serializer_class = ParametresTrailerSerializer
    permission_classes = [permissions.IsAdminUser]


class CreateLocationCargoAPIView(ListCreateAPIView):
    queryset = LocationCargo.objects.all()
    serializer_class = LocationCargoSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateLocationCargoAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LocationCargo.objects.all()
    serializer_class = LocationCargoSerializer
    permission_classes = [permissions.IsAdminUser]

# class CreateDealStatusView(ListCreateAPIView):
#     queryset = DealStatus.objects.all()
#     serializer_class = DealStatusSerializer
#     # permission_classes = (permissions.IsAdminUser)
#
#
# class UpdateDealStatusView(RetrieveUpdateDestroyAPIView):
#     queryset = DealStatus.objects.all()
#     serializer_class = DealStatusSerializer
#     # permission_classes = (permissions.IsAdminUser)


# class CreateSubclassHazardView(ListCreateAPIView):
#     queryset = SubclassHazard.objects.all()
#     serializer_class = SubclassHazardSerializer
#     # permission_classes = (permissions.IsAdminUser)
#
#
# class UpdateSubclassHazardView(RetrieveUpdateDestroyAPIView):
#     queryset = SubclassHazard.objects.all()
#     serializer_class = SubclassHazardSerializer
#     # permission_classes = (permissions.IsAdminUser)
