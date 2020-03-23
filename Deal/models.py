from django.db import models
from django.conf import settings
from app.models import Clients, Driver, Manager
import datetime


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
        return self.value

    class Meta:
        verbose_name = "Ед.изм."
        verbose_name_plural = "Ед.изм."


class Volume(models.Model):
    """
    Класс объём
    """

    width = models.IntegerField(default=1, verbose_name='Ширина')
    height = models.IntegerField(default=1, verbose_name='Высота')
    length = models.IntegerField(default=1, verbose_name='Длина')
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True, verbose_name='Ед.измерения')

    def __str__(self):
        return '{}'.format(self.width)

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
        return '{}'.format(self.heightNoLess)

    class Meta:
        verbose_name = "Параметр прицепа"
        verbose_name_plural = "Параметры прицепа"

class LocationCargo(models.Model):
    """
    Класс местоположения груза
    """
    ORDER_STATUS_CHOICES = (
        ('Отправлен', 'Отправлен'),
        ('Получен', 'Получен'),
        ('Подтвержден', 'Подтвержден'),
        ('Запрошен повтор отправки', 'Запрошен повтор отправки'),
    )

    latitude = models.FloatField(default=0.0, verbose_name='Широта')
    longitude = models.FloatField(default=0.0, verbose_name='Долгота')
    sendingTimeCoordinates = models.CharField(max_length=125 ,verbose_name='Время отправки координат', default=datetime.datetime.now().time() )
    locationCoordinatesStatus = models.CharField(max_length=125 ,choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][1],
                                                  verbose_name='Статус координат местоположения')

    def __str__(self):
        return '{}'.format(self.locationCoordinatesStatus)

    class Meta:
        verbose_name = "Местоположение груза"
        verbose_name_plural = "Местоположения грузов"


class Order(models.Model):
    """
    Класс сделка
    """
    NEW = 0
    CONCLUDED = 1
    LOADING = 2
    TRANSPORTING = 3
    UNLOADING = 4
    COMPLETED = 5
    CANCELLED = 6

    ORDER_STATUS_CHOICES = (
        ('NEW', 'Новая'),
        ('CONCLUDED', 'Заключена'),
        ('LOADING', 'Погрузка'),
        ('TRANSPORTING', 'Транспортировка'),
        ('UNLOADING', 'Выгрузка'),
        ('COMPLETED', 'Завершена'),
        ('CANCELLED', 'Отменена')
    )
    numberOrder = models.IntegerField(verbose_name='Номер заказа клиента')
    priceClient = models.IntegerField(default=0, verbose_name='Цена клиента')
    companyProfit = models.IntegerField(default=0, verbose_name='Прибыль компании')
    fromOrder = models.CharField(max_length=20, blank=True, verbose_name='Дата начала заказа', default=datetime.date.today)
    toOrder = models.CharField(max_length=20, blank=True, verbose_name='Дата завершения заказа', default='')
    dateLoading = models.DateField(blank=True, verbose_name='Дата погрузки')
    dateUnloading = models.DateField(blank=True, verbose_name='Дата выгрузки')
    autoReleaseYear = models.IntegerField(verbose_name='Год выпуска авто')
    countPallet = models.IntegerField(verbose_name='Количество паллет')
    stateAwning = models.CharField(max_length=100, verbose_name='Состояние тента')
    requirementsLoading = models.CharField(max_length=100, verbose_name='Требования погрузки')
    typeAuto = models.ForeignKey(TypeAuto, on_delete=models.SET_NULL, null=True, related_name='typeAuto',
                                 verbose_name='Тип авто', )
    typeLoading = models.ForeignKey(TypeLoading, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='typeLoading', verbose_name='Тип погрузки')
    typeCargo = models.ForeignKey(TypeCargo, on_delete=models.SET_NULL, null=True, related_name='typeCargo',
                                  verbose_name='Тип груза')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, related_name='volume',
                               verbose_name='Объём')
    orderStatus = models.CharField(max_length=125, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_CHOICES[0][1], verbose_name='Статус заказа')
    parametresTrailer = models.ForeignKey(ParametresTrailer, on_delete=models.SET_NULL, null=True,
                                          related_name='parametresTrailer', verbose_name='Параметры заказа')
    locationCargo = models.ForeignKey(LocationCargo, on_delete=models.SET_NULL, null=True, related_name='locationCargo',
                                      verbose_name='Местоположение груза',)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='Пользователь',
                                verbose_name='Клиент', unique=False)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='driver', verbose_name='Водитель')

    def __str__(self):
        return '{}'.format(self.user)

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"


