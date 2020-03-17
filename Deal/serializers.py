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
        fields = ['locationCoordinates', 'sendingTimeCoordinates', 'locationCoordinatesStatus']

# class DealStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DealStatus
#         fields = ['new', 'concluded', 'loading', 'transportation', 'unloading', 'completed', 'cancel']
#


class OrderUpdateSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):

        instance.numberOrderFromClient = validated_data.get('numberOrderFromClient', instance.numberOrderFromClient)
        instance.priceClient = validated_data.get('priceClient', instance.priceClient)
        instance.companyProfit = validated_data.get('companyProfit', instance.companyProfit)
        #instance.fromOrder = validated_data.get('fromOrder', instance.fromOrder)
        #instance.toOrder = validated_data.get('toOrder', instance.toOrder)
        #instance.dateLoading = validated_data.get('dateLoading', instance.dateLoading)
        #instance.dateUnloading = validated_data.get('dateUnloading', instance.dateUnloading)
        instance.autoReleaseYear = validated_data.get('autoReleaseYear', instance.autoReleaseYear)
        #instance.countPallet = validated_data.get('countPallet', instance.countPallet)
        instance.stateAwning = validated_data.get('stateAwning', instance.stateAwning)
        instance.requirementsLoading = validated_data.get('requirementsLoading', instance.requirementsLoading)
        instance.typeAuto = validated_data.get('typeAuto', instance.typeAuto)
        #instance.typeLoading = validated_data.get('typeLoading', instance.typeLoading)
        instance.typeCargo = validated_data.get('typeCargo', instance.typeCargo)
        #instance.subclassHazard = validated_data.get('subclassHazard', instance.subclassHazard)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.volume = validated_data.get('volume', instance.volume)
        instance.orderStatus = validated_data.get('orderStatus', instance.orderStatus)
        #instance.parametresTrailer = validated_data.get('parametresTrailer', instance.parametresTrailer)
        instance.locationCargo = validated_data.get('locationCargo', instance.locationCargo)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return  instance

    class Meta:
        model = Order
        fields = '__all__'


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
    owner = serializers.CharField(source='owner.__str__')

    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('numberOrderFromClient', 'autoReleaseYear', 'stateAwning', 'requirementsLoading',
                  'typeAuto', 'typeCargo', 'weight', 'weightMeasurementUnit', 'volume', 'orderStatus',
                  'locationCargo', 'owner')