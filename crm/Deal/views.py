from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
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


class CreateTypeAutoView(ListCreateAPIView):
    queryset = TypeAuto.objects.all()
    serializer_class = TypeAutoSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateTypeLoadingView(ListCreateAPIView):
    queryset = TypeLoading.objects.all()
    serializer_class = TypeLoadingSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateUnitsView(ListCreateAPIView):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateWeightView(ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateVolumeView(ListCreateAPIView):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateParametresTrailerView(ListCreateAPIView):
    queryset = ParametresTrailer.objects.all()
    serializer_class = ParametresTrailerSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateLocationCargoView(ListCreateAPIView):
    queryset = LocationCargo.objects.all()
    serializer_class = LocationCargoSerializer
    # permission_classes = (permissions.IsAdminUser)


class CreateDealStatusView(ListCreateAPIView):
    queryset = DealStatus.objects.all()
    serializer_class = DealStatusSerializer
    # permission_classes = (permissions.IsAdminUser)
