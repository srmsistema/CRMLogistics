from rest_framework import serializers
from .models import *


# class SubclassHazardSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model =  SubclassHazard
#         fields = ['description',]
#

class TypeCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeCargo
        fields = ['type', ]

class TypeAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAuto
        fields = ['type', ]

class TypeLoadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAuto
        fields = ['type', ]

class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ['value', ]


# class WeightSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Weight
#         fields = ['minimum', 'maximum', 'unit']

class VolumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volume
        fields = ['width', 'height', 'length', 'unit']

class ParametresTrailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParametresTrailer
        fields = ['heightNoLess', 'lackOfSmell', 'lackOfThings', 'woodenFloor', 'dopple', 'demin', 'connik']

class LocationCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationCargo
        fields = ['longitude', 'latitude', 'sendingTimeCoordinates', ]
                  # 'locationCoordinatesStatus']

# class DealStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DealStatus
#         fields = ['new', 'concluded', 'loading', 'transportation', 'unloading', 'completed', 'cancel']
#

class OrderListSerializer(serializers.ModelSerializer):

    typeAuto = TypeAutoSerializer(many=False, read_only=True)
    typeLoading = TypeLoadingSerializer(many=False, read_only=True)
    typeCargo = TypeCargoSerializer(many=False, read_only=True)
    # subclassHazard = SubclassHazardSerializer(many=False, read_only=True)
    # weight = WeightSerializer(many=False, read_only=True)
    volume = VolumeSerializer(many=False, read_only=True)
    # dealStatus = DealStatusSerializer(many=False, read_only=True)
    parametresTrailer = ParametresTrailerSerializer(many=False, read_only=True)
    locationCargo= LocationCargoSerializer(many=False, read_only=True)
    user = serializers.CharField(source='owner.__str__')

    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    numberOrderFromClient = serializers.IntegerField(source='count_orders_number', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'