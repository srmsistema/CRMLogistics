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

# class ParametresTrailerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ParametresTrailer
#         fields = ['heightNoLess', 'lackOfSmell', 'lackOfThings', 'woodenFloor', 'dopple', 'demin', 'connik']

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


class OrderDriverListSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer(many=False)
    # parametresTrailer = ParametresTrailerSerializer(many=False)
    locationCargo = LocationCargoSerializer(many=False)

    class Meta:
        model = Order
        exclude = ['companyProfit']

class OrderDriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['numberOrder', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear',
                  'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                  'volume', 'locationCargo',
                  'user', 'driver', 'orderStatus', 'fromOrder', 'toOrder']
        read_only_fields = fields

class OrderClientCreateSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    # parametresTrailer = ParametresTrailerSerializer()
    locationCargo = LocationCargoSerializer()


    class Meta:
        model = Order
        fields = ['numberOrder', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear', 'stateAwning', 'requirementsLoading',
                  'typeAuto', 'typeLoading', 'typeCargo', 'weight', 'volume', 'locationCargo',  'user']
        read_only_fields = ['user', 'driver', 'orderStatus', 'fromOrder', 'toOrder', 'companyProfit']

    def create(self, validated_data):
        volume_data = validated_data.pop('volume')
        # parametresTrailer_data = validated_data.pop('parametresTrailer')
        locationCargo_data = validated_data.pop('locationCargo')

        volume = Volume.objects.create(**volume_data)
        # parametresTrailer = ParametresTrailer.objects.create(**parametresTrailer_data)
        locationCargo = LocationCargo.objects.create(**locationCargo_data)

        # order = Order.objects.create(volume=volume, parametresTrailer=parametresTrailer, locationCargo=locationCargo,**validated_data)
        order = Order.objects.create(volume=volume, locationCargo=locationCargo, **validated_data)

        return order