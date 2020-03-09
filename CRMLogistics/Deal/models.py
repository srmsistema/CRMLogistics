from django.db import models
from django.conf import settings

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
        return self.value

    class Meta:
        verbose_name = "Ед.изм."
        verbose_name_plural = "Ед.изм."


# class Weight(models.Model):
#     """
#     Класс вес
#     """
#
#     minimum = models.IntegerField(default=1)
#     maximum = models.IntegerField(default=10)
#     unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)
#
#     def __str__(self):
#         return self.minimum
#
#     class Meta:
#         verbose_name = "Вес"
#         verbose_name_plural = "Вес"


class Volume(models.Model):
    """
    Класс объём
    """

    width = models.IntegerField(default=1, verbose_name='Ширина')
    height = models.IntegerField(default=1, verbose_name='Высота')
    length = models.IntegerField(default=1, verbose_name='Длина')
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True, verbose_name='Ед.измерения')

    def __str__(self):
        return self.width

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
        return self.heightNoLess

    class Meta:
        verbose_name = "Параметр прицепа"
        verbose_name_plural = "Параметры прицепа"


class LocationCoordinatesStatus(models.Model):
    """
    Класс статус координат местоположения
    """

    status = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус координата"
        verbose_name_plural = "Статусы координат"


class LocationCargo(models.Model):
    """
    Класс местоположения груза
    """

    locationCoordinates = models.CharField(max_length=255, verbose_name='Координаты местоположения')
    sendingTimeCoordinates = models.TextField(verbose_name='Время отправки координат')
    locationCoordinatesStatus = models.ForeignKey(LocationCoordinatesStatus, on_delete=models.SET_NULL, null=True, verbose_name='Статус координат местоположения')

    def __str__(self):
        return self.locationCoordinates

    class Meta:
        verbose_name = "Местоположение груза"
        verbose_name_plural = "Местоположения грузов"

#
# class DealStatus(models.Model):
#     """
#     Класс Статус сделки
#     """
#
#     new = models.BooleanField(default=False)
#     concluded = models.BooleanField(default=False)
#     loading = models.BooleanField(default=False)
#     transportation = models.BooleanField(default=False)
#     unloading = models.BooleanField(default=False)
#     completed = models.BooleanField(default=False)
#     cancel = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.new
#
#     class Meta:
#         verbose_name = "Статус сделки"
#         verbose_name_plural = "Статусы сделок"


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
        (NEW, 'Новая'),
        (CONCLUDED, 'Заключена'),
        (LOADING, 'Погрузка'),
        (TRANSPORTING, 'Транспортировка'),
        (UNLOADING, 'Выгрузка'),
        (COMPLETED, 'Завершена'),
        (CANCELLED, 'Отменена')
    )
    numberOrderFromClient = models.CharField(max_length=50, verbose_name='Номер заказа клиента', )
    priceClient = models.IntegerField(default=0, verbose_name='Цена клиента')
    companyProfit = models.IntegerField(default=0, verbose_name='Прибыль компании')
    fromOrder = models.CharField(max_length=255, blank=True, verbose_name='Дата начала заказа')
    toOrder = models.CharField(max_length=255, blank=True, verbose_name='Дата завершения заказа')
    dateLoading = models.DateField(blank=True, verbose_name='Дата погрузки')
    dateUnloading = models.DateField(blank=True, verbose_name='Дата выгрузки')
    autoReleaseYear = models.IntegerField(verbose_name='Год выпуска авто')
    countPallet = models.IntegerField(verbose_name='Количество паллет')
    stateAwning = models.CharField(max_length=100, verbose_name='Состояние тента')
    requirementsLoading = models.CharField(max_length=100, verbose_name='Требования погрузки')
    typeAuto = models.ForeignKey(TypeAuto, on_delete=models.SET_NULL, null=True, related_name='typeAuto', verbose_name='Тип авто')
    typeLoading = models.ForeignKey(TypeLoading, on_delete=models.SET_NULL, null=True, blank=True, related_name='typeLoading', verbose_name='Тип погрузки')
    typeCargo = models.ForeignKey(TypeCargo,on_delete=models.SET_NULL, null=True, related_name='typeCargo', verbose_name='Тип груза')
    weight = models.IntegerField(default=0, verbose_name='Вес')
    #subclassHazard = models.ForeignKey(SubclassHazard, on_delete=models.SET_NULL, null=True, related_name='subclassHazard')
    weightMeasurementUnit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True, related_name='weightMeasurementUnit', verbose_name='Ед. изм.')
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, related_name='volume', verbose_name='Объём')
    orderStatus = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=None, blank=True, verbose_name='Статус заказа')
    parametresTrailer = models.ForeignKey(ParametresTrailer, on_delete=models.SET_NULL, null=True, related_name='parametresTrailer', verbose_name='Параметры заказа')
    locationCargo = models.ForeignKey(LocationCargo, on_delete=models.SET_NULL, null=True, related_name='locationCargo', verbose_name='Местоположение груза')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='user', verbose_name='Заказчик')

    def __str__(self):
        return self.numberOrderFromClient

    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"