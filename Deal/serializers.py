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
    unit = serializers.StringRelatedField()

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
    volume = VolumeSerializer()
    # parametresTrailer = ParametresTrailerSerializer()
    locationCargo = LocationCargoSerializer()
    owner = serializers.StringRelatedField()
    typeAuto = serializers.StringRelatedField(many=False, read_only=True)
    typeLoading = serializers.StringRelatedField(many=False, read_only=True)
    typeCargo = serializers.StringRelatedField(many=False, read_only=True)
    orderStatus = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    # parametresTrailer = ParametresTrailerSerializer()
    locationCargo = LocationCargoSerializer()
    owner = serializers.StringRelatedField()
    typeAuto = serializers.StringRelatedField(many=False, read_only=True)
    typeLoading = serializers.StringRelatedField(many=False, read_only=True)
    typeCargo = serializers.StringRelatedField(many=False, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'