from rest_framework import serializers
from .models import *
from app.serializers import ClientSerializer


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
        fields = ['latitude', 'longitude', 'sendingTimeCoordinates', 'locationCoordinatesStatus']
        read_only_fields = ['locationCoordinatesStatus', 'sendingTimeCoordinates']










class OrderSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    parametresTrailer = ParametresTrailerSerializer()
    locationCargo = LocationCargoSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class OrderDriverListSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer(many=False)
    parametresTrailer = ParametresTrailerSerializer(many=False)
    locationCargo = LocationCargoSerializer(many=False)

    class Meta:
        model = Order
        exclude = ['companyProfit']

class OrderDriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['numberOrder', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear', 'countPallet',
                  'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                  'volume', 'parametresTrailer', 'locationCargo',
                  'user', 'driver', 'orderStatus', 'parametresTrailer', 'fromOrder', 'toOrder']
        read_only_fields = fields

class OrderClientCreateSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    parametresTrailer = ParametresTrailerSerializer()
    locationCargo = LocationCargoSerializer()


    class Meta:
        model = Order
        fields = ['numberOrder', 'priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear', 'countPallet', 'stateAwning', 'requirementsLoading',
                  'typeAuto', 'typeLoading', 'typeCargo', 'weight', 'volume', 'parametresTrailer', 'locationCargo',  'user']
        read_only_fields = ['user', 'driver', 'orderStatus', 'parametresTrailer', 'fromOrder', 'toOrder', 'companyProfit']

    def create(self, validated_data):
        volume_data = validated_data.pop('volume')
        parametresTrailer_data = validated_data.pop('parametresTrailer')
        locationCargo_data = validated_data.pop('locationCargo')

        volume = Volume.objects.create(**volume_data)
        parametresTrailer = ParametresTrailer.objects.create(**parametresTrailer_data)
        locationCargo = LocationCargo.objects.create(**locationCargo_data)

        order = Order.objects.create(volume=volume, parametresTrailer=parametresTrailer, locationCargo=locationCargo,**validated_data)

        return order