from builtins import super, int
from django.db import models
from django.conf import settings
from django.utils import timezone
from app.models import User, Driver
import datetime
import re

# class SubclassHazard(models.Model):
#     """
#     Класс опасности
#     """
#
#     description = models.CharField(max_length=255, verbose_name='Описание')
#
#     def __str__(self):
#         return self.description
#
#     class Meta:
#         verbose_name = "Опасность"
#         verbose_name_plural = "Опасности"



class TypeCargo(models.Model):
    """
    Класс тип груза
    """

    type = models.CharField(max_length=50, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип груза"
        verbose_name_plural = "Типы грузов"


class TypeAuto(models.Model):
    """
    Класс тип автомобиля
    """

    type = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип авто"
        verbose_name_plural = "Типы автомобиля"


class TypeLoading(models.Model):
    """
    Класс тип погрузки
    """

    type = models.CharField(max_length=100, verbose_name='Тип')

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип погрузки"
        verbose_name_plural = "Типы погрузки"


class Units(models.Model):
    """
    Класс единицы измерения
    """

    value = models.CharField(max_length=50, verbose_name='Значение')

    def __str__(self):
        return "%s"%(self.value)

    class Meta:
        verbose_name = "Ед.изм."
        verbose_name_plural = "Ед.изм."


class Volume(models.Model):
    """
    Класс объём
    """

    width = models.FloatField(default=0.0, verbose_name='Ширина')
    height = models.FloatField(default=0.0, verbose_name='Высота')
    length = models.FloatField(default=0.0, verbose_name='Длина')
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True, verbose_name='Ед.изм. объёма')

    def count_volume(self):
        return "%s %s " % (self.width * self.height * self.length, self.unit)

    def __str__(self):
        return "%s %s" % (self.count_volume(), self.unit)

    class Meta:
        verbose_name = "Объём"
        verbose_name_plural = "Объёмы"


class ParametresTrailer(models.Model):
    """
    Класс параметры прицепа
    """

    heightNoLess = models.IntegerField(default=1, verbose_name='Высота не меньше')
    lackOfSmell = models.BooleanField(default=False, verbose_name='Отсутствие запахов')
    lackOfThings = models.BooleanField(default=False, verbose_name='Отсутствие выступающих вещей')
    woodenFloor = models.BooleanField(default=False, verbose_name='Деревянный пол')
    dopple = models.BooleanField(default=False, verbose_name='Наличие допельштоков')
    demin = models.IntegerField(default=1, verbose_name='Кол-во ремней')
    connik = models.IntegerField(default=1, verbose_name='Кол-во конников')

    def __str__(self):
        return "Высота не меньше: %s \n Кол-во ремней: %s \n Кол-во конников: %s" % (self.heightNoLess, self.demin, self.connik)

    class Meta:
        verbose_name = "Параметр прицепа"
        verbose_name_plural = "Параметры прицепа"


# class LocationCoordinatesStatus(models.Model):
#     """
#     Класс статус координат местоположения
#     """
#
#     status = models.CharField(max_length=50, verbose_name='Статус')
#
#     def __str__(self):
#         return self.status
#
#     class Meta:
#         verbose_name = "Статус координата"
#         verbose_name_plural = "Статусы координат"


class LocationCargo(models.Model):
    """
    Класс местоположения груза
    """

    # locationCoordinates = models.CharField(max_length=255, verbose_name='Координаты местоположения')
    # longitude = models.FloatField(default=0.0, verbose_name='Долгота')
    # latitude = models.FloatField(default=0.0, verbose_name='Широта')
    address = models.CharField(max_length=255, default="", blank=False, verbose_name="Адрес")
    sendingTimeCoordinates = models.CharField(max_length=255, default=datetime.datetime.now().time(), blank=True, verbose_name='Время отправки координат')
    # locationCoordinatesStatus = models.ForeignKey(LocationCoordinatesStatus, on_delete=models.SET_NULL, null=True, verbose_name='Статус координат местоположения')

    # def save(self, *args, **kwargs):
    #     sendingTime =
    #     self.sendingTimeCoordinates = sendingTime
    #     super(LocationCargo, self).save(*args, **kwargs)

    def __str__(self):
        return "%s, %s" % (self.address, self.sendingTimeCoordinates)

    class Meta:
        verbose_name = "Местоположение груза"
        verbose_name_plural = "Местоположения грузов"


class StateAwning(models.Model):
    noHoles = models.BooleanField(default=False, verbose_name="Без дыр")
    noGaps = models.BooleanField(default=False, verbose_name="Без щелей")
    dry = models.BooleanField(default=False, verbose_name="Сухой")
    noPatches = models.BooleanField(default=False, verbose_name="Отсутствие заплаток")

    class Meta:
        verbose_name = 'Состояние тента'
        verbose_name_plural = 'Состояния тентов'

    def __str__(self):
        noHoles = self.noHoles
        noGaps =self.noGaps
        dry = self.dry
        noPatches = self.noPatches
        state = ''
        if noHoles:
            state += 'Без дыр, '
        if noGaps:
            state += 'Без щелей, '
        if dry:
            state += 'Сухой, '
        if noPatches:
            state += 'Без заплаток, '

        state = state[0] + re.sub( '(?<!^)(?=[A-Z])', '_', state[1:] ).lower()
        print(state)
        return state[:-2]


class Order(models.Model):
    """
    Класс сделка
    """


    ORDER_STATUS_CHOICES = (
        ('Новая', 'Новая'),
        ('Заключена', 'Заключена'),
        ('Погрузка', 'Погрузка'),
        ('Транспортировка', 'Транспортировка'),
        ('Выгрузка', 'Выгрузка'),
        ('Завершена', 'Завершена'),
        ('Отменена', 'Отменена')
    )
    name = models.CharField(default='', blank=True,  max_length=100, verbose_name='Название')
    # numberOrderFromClient = models.IntegerField(default=0, editable=False, verbose_name='Номер заказа клиента')
    priceClient = models.IntegerField(default=0, verbose_name='Цена клиента')
    companyProfit = models.IntegerField(default=0, verbose_name='Прибыль компании')
    fromOrder = models.DateField(blank=True, null=True, verbose_name='Дата начала заказа')
    toOrder = models.DateField(blank=True, null=True,  verbose_name='Дата завершения заказа')
    dateLoading = models.DateField(blank=True, null=True, verbose_name='Дата погрузки')
    dateUnloading = models.DateField(blank=True, null=True, verbose_name='Дата выгрузки')
    autoReleaseYear = models.IntegerField(default=0, verbose_name='Год выпуска авто')
    # countPallet = models.IntegerField(default=0, verbose_name='Количество паллет')
    stateAwning = models.ForeignKey(StateAwning, on_delete=models.SET_NULL, null=True, blank=True, related_name='stateAwning', verbose_name='Состояние тента')
    requirementsLoading = models.CharField(default='', blank=True, max_length=100, verbose_name='Требования погрузки')
    typeAuto = models.ForeignKey(TypeAuto, on_delete=models.SET_NULL, null=True, related_name='typeAuto', verbose_name='Тип авто')
    typeLoading = models.ForeignKey(TypeLoading, on_delete=models.SET_NULL, null=True, blank=True, related_name='typeLoading', verbose_name='Тип погрузки')
    typeCargo = models.ForeignKey(TypeCargo,on_delete=models.SET_NULL, null=True, related_name='typeCargo', verbose_name='Тип груза')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    #subclassHazard = models.ForeignKey(SubclassHazard, on_delete=models.SET_NULL, null=True, related_name='subclassHazard')
    weightMeasurementUnit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True, related_name='weightMeasurementUnit', verbose_name='Ед. изм. веса')
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, related_name='volume', verbose_name='Объём')
    orderStatus = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][0], blank=True, verbose_name='Статус заказа')
    # parametresTrailer = models.ForeignKey(ParametresTrailer, on_delete=models.SET_NULL, null=True, related_name='parametresTrailer', verbose_name='Параметры заказа')
    locationCargo = models.ForeignKey(LocationCargo, on_delete=models.SET_NULL, null=True, related_name='locationCargo', verbose_name='Местоположение груза')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user', verbose_name='Заказчик')
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True, related_name="driver", verbose_name="Водитель")

    def save(self, *args, **kwargs):
        if self.orderStatus == self.ORDER_STATUS_CHOICES[1][0]:
            self.fromOrder = datetime.date.today()
        elif self.orderStatus == self.ORDER_STATUS_CHOICES[5][0]:
            self.toOrder = datetime.date.today()
        elif self.orderStatus == self.ORDER_STATUS_CHOICES[2][0]:
            self.dateLoading = datetime.date.today()
        elif self.orderStatus == self.ORDER_STATUS_CHOICES[4][0]:
            self.dateUnloading = datetime.date.today()

        super(Order, self).save(*args, **kwargs)


    def status(self):
        # return '%s' % self.ORDER_STATUS_CHOICES[int(self.orderStatus)][1]
        return '%s' % self.orderStatus
    status.short_description = 'Статус заявки'

    def __str__(self):
        return "%s" % self.user

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"