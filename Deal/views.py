from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Driver
from .serializers import *
from rest_framework import permissions
from .permissions import IsManager, IsClient, IsDriver
from rest_framework.response import Response
from rest_framework import status


class ListOrderAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser | IsClient | IsManager | IsDriver]

    def get(self, request, *args, **kwargs):
        if request.user.is_staff and request.user:
            serializers = OrderSerializer(Order.objects.all(), many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        elif request.user.is_client and request.user:
            serializers = OrderSerializer(Order.objects.filter(user=self.request.user), many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        elif request.user.is_manager and request.user:
            serializers = OrderSerializer(Order.objects.filter(user=self.request.user), many=True)
            return Response(serializers.data, status.HTTP_200_OK)
        elif request.user.is_driver and request.user:
            serializers = OrderDriverListSerializer(Order.objects.all(), many=True)
            return Response(serializers.data, status.HTTP_200_OK)



class ListOrderDriverAPIView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDriverListSerializer
    permission_classes = [IsDriver]

    def get(self, request, *args, **kwargs):
        serializers = OrderDriverListSerializer(Order.objects.filter(driver__user=request.user), many=True)
        return Response(serializers.data, status.HTTP_200_OK)


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderClientCreateSerializer
    permission_classes = [IsManager | IsClient]

    def perform_create(self, serializer):
        if self.request.user.is_manager and self.request.user:
            return serializer.save(user=self.request.user)
        elif self.request.user.is_client and self.request.user:
            return serializer.save(user=self.request.user)


class UpdateOrderAPIView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDriverUpdateSerializer
    permission_classes = [permissions.IsAdminUser | IsDriver]

    def perform_update(self, serializer):
        if self.request.user and self.request.user.is_driver:
            driver = Driver.objects.get(user=self.request.user)
            serializer.save(orderStatus=Order.CONCLUDED)
            return serializer.save(driver=driver)


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

#
# class CreateParametresTrailerAPIView(ListCreateAPIView):
#     queryset = ParametresTrailer.objects.all()
#     serializer_class = ParametresTrailerSerializer
#     permission_classes = [permissions.IsAdminUser]


# class UpdateParametresTrailerAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = ParametresTrailer.objects.all()
#     serializer_class = ParametresTrailerSerializer
#     permission_classes = [permissions.IsAdminUser]


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


