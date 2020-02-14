from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView, \
    ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from rest_framework import permissions


class ListDealView(ListAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class CreateDealView(CreateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    # permission_classes = (permissions.IsAuthenticated)

    # def perform_create(self, serializer):
    #     serializer.save(owner = self.request.user)


class UpdateDealView(RetrieveUpdateAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    permission_classes = (permissions.IsAdminUser)


class DeleteDealView(RetrieveDestroyAPIView):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateTypeCargoView(ListCreateAPIView):
    queryset = TypeCargo.objects.all()
    serializer_class = TypeCargoSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateTypeCargoView(RetrieveUpdateDestroyAPIView):
    queryset = TypeCargo.objects.all()
    serializer_class = TypeCargoSerializer


class CreateTypeAutoView(ListCreateAPIView):
    queryset = TypeAuto.objects.all()
    serializer_class = TypeAutoSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateTypeAutoView(RetrieveUpdateDestroyAPIView):
    queryset = TypeAuto.objects.all()
    serializer_class = TypeAutoSerializer


class CreateTypeLoadingView(ListCreateAPIView):
    queryset = TypeLoading.objects.all()
    serializer_class = TypeLoadingSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateTypeLoadingView(RetrieveUpdateDestroyAPIView):
    queryset = TypeLoading.objects.all()
    serializer_class = TypeLoadingSerializer


class CreateUnitsView(ListCreateAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateUnitsView(RetrieveUpdateDestroyAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer


class CreateWeightView(ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateWeightView(RetrieveUpdateDestroyAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer


class CreateVolumeView(ListCreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    # permission_classes = (permissions.IsAdminUser)

class UpdateVolumeView(RetrieveDestroyAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer

class CreateParametresTrailerView(ListCreateAPIView):
    queryset = ParametresTrailer.objects.all()
    serializer_class = ParametresTrailerSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateParametresTrailerView(RetrieveUpdateDestroyAPIView):
    queryset = ParametresTrailer.objects.all()
    serializer_class = ParametresTrailerSerializer


class CreateLocationCargoView(ListCreateAPIView):
    queryset = LocationCargo.objects.all()
    serializer_class = LocationCargoSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateLocationCargoView(RetrieveUpdateDestroyAPIView):
    queryset = LocationCargo.objects.all()
    serializer_class = LocationCargoSerializer


class CreateDealStatusView(ListCreateAPIView):
    queryset = DealStatus.objects.all()
    serializer_class = DealStatusSerializer
    # permission_classes = (permissions.IsAdminUser)


class UpdateDealStatusView(RetrieveUpdateDestroyAPIView):
    queryset = DealStatus.objects.all()
    serializer_class = DealStatusSerializer