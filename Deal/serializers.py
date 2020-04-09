from rest_framework import serializers
from .models import *
from app.serializers import DriversSerializer, DriversSerializer2

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
    # unit = serializers.StringRelatedField()

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
        fields = ['address', 'sendingTimeCoordinates', ]
        read_only_fields = ['sendingTimeCoordinates', ]

    # def create(self, validated_data):
    #     location = LocationCargo.objects.create(sendingTimeCoordinates=timezone.now(), **validated_data)
    #     return location


class StateAwningSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateAwning
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    # parametresTrailer = ParametresTrailerSerializer()
    locationCargo = serializers.StringRelatedField()
    user = serializers.StringRelatedField()
    typeAuto = serializers.StringRelatedField(many=False, read_only=True)
    typeLoading = serializers.StringRelatedField(many=False, read_only=True)
    typeCargo = serializers.StringRelatedField(many=False, read_only=True)
    orderStatus = serializers.StringRelatedField(many=False, read_only=True)
    stateAwning = StateAwningSerializer()
    driver = DriversSerializer2()

    class Meta:
        model = Order
        fields = '__all__'


class OrderDriverListSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer(many=False)
    # parametresTrailer = ParametresTrailerSerializer(many=False)

    class Meta:
        model = Order
        exclude = ['companyProfit']


class OrderDriverUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear',
                  'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                  'volume', 'locationCargo', 'user', 'driver', 'orderStatus', 'fromOrder', 'toOrder']

        read_only_fields = ['priceClient', 'dateLoading', 'dateUnloading', 'autoReleaseYear',
                  'stateAwning', 'requirementsLoading', 'typeAuto', 'typeLoading', 'typeCargo', 'weight',
                  'volume', 'locationCargo', 'user', 'driver', 'fromOrder', 'toOrder']

        # def update(self, instance, validated_data):
        #     orderStatus = validated_data.get('orderStatus', instance.orderStatus)
        #     if orderStatus == 'Заключена':
        #         instance.fromOrder = datetime.date.today
        #     if orderStatus == 'Погрузка':
        #         instance.dateLoading = datetime.date.today
        #     if orderStatus == 'Выгрузка':
        #         instance.dateUnloading = datetime.date.today
        #     if orderStatus == 'Завершена':
        #         instance.toOrder = datetime.date.today
        #     return instance.save()


class OrderClientCreateSerializer(serializers.ModelSerializer):

    volume = VolumeSerializer()
    # parametresTrailer = ParametresTrailerSerializer()
    stateAwning = StateAwningSerializer()
    locationCargo = LocationCargoSerializer()

    class Meta:
        model = Order
        fields = ['priceClient', 'requirementsLoading', 'typeCargo', 'typeAuto', 'autoReleaseYear',
                  'typeLoading', 'stateAwning', 'weight',
                  'weightMeasurementUnit', 'volume', 'locationCargo',  'user']
        read_only_fields = ['user', 'driver', 'orderStatus', 'fromOrder', 'toOrder']

    def create(self, validated_data):
        volume_data = validated_data.pop('volume')
        # parametresTrailer_data = validated_data.pop('parametresTrailer')
        locationCargo_data = validated_data.pop('locationCargo')
        stateAwning_data = validated_data.pop('stateAwning')
        volume = Volume.objects.create(**volume_data)
        # parametresTrailer = ParametresTrailer.objects.create(**parametresTrailer_data)
        stateAwning = StateAwning.objects.create(**stateAwning_data)
        locationCargo = LocationCargo.objects.create(**locationCargo_data)
        # order = Order.objects.create(volume=volume, parametresTrailer=parametresTrailer, locationCargo=locationCargo,**validated_data)
        order = Order.objects.create(volume=volume, locationCargo=locationCargo, stateAwning=stateAwning, **validated_data)

        return order