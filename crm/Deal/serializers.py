from rest_framework.serializers import ModelSerializer
from .models import *

class DealSerializer(ModelSerializer):

    class Meta:
        model = Deal
        fields = [
            'numberDealFromClient',
            'priceClient',
            'companyProfit',
            'fromDeal',
            'toDeal',
            'dateLoading',
            'dateUnloading',
            'autoReleaseYear',
            'countPallet',
            'stateAwning',
            'requirementsLoading',
            'typeAuto',
            'typeLoading',
            'typeCargo',
            'subclassHazard',
            'weight',
            'volume',
            'dealStatus',
            'parametresTrailer',
            'locationCargo',
            'owner'
        ]

class SubclassHazardSerializer(ModelSerializer):

    class Meta:
        model =  SubclassHazard
        fields = ['description',]


class TypeCargoSerializer(ModelSerializer):
    class Meta:
        model = TypeCargo
        fields = ['type', ]

class TypeAutoSerializer(ModelSerializer):
    class Meta:
        model = TypeAuto
        fields = ['type', ]

class TypeLoadingSerializer(ModelSerializer):
    class Meta:
        model = TypeAuto
        fields = ['type', ]

class UnitsSerializer(ModelSerializer):
    class Meta:
        model = Units
        fields = ['value', ]


class WeightSerializer(ModelSerializer):
    class Meta:
        model = Weight
        fields = ['minimum', 'maximum', 'unit']

class VolumeSerializer(ModelSerializer):
    class Meta:
        model = Volume
        fields = ['width', 'height', 'length', 'unit']

class ParametresTrailerSerializer(ModelSerializer):
    class Meta:
        model = ParametresTrailer
        fields = ['heightNoLess', 'lackOfSmell', 'lackOfThings', 'woodenFloor', 'dopple', 'demin', 'connik']

class LocationCargoSerializer(ModelSerializer):
    class Meta:
        model = LocationCargo
        fields = ['locationCoordinates', 'sendingTimeCoordinates', 'locationCoordinatesStatus']

class DealStatusSerializer(ModelSerializer):
    class Meta:
        model = DealStatus
        fields = ['new', 'concluded', 'loading', 'transportation', 'unloading', 'completed', 'cancel']

