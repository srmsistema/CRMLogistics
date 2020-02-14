from django.db import models

class SubclassHazard(models.Model):
    """
    Класс опасности
    """

    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Опасность"
        verbose_name_plural = "Опасности"


class TypeCargo(models.Model):
    """
    Класс тип груза
    """

    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип груза"
        verbose_name_plural = "Типы грузов"


class TypeAuto(models.Model):
    """
    Класс тип автомобиля
    """

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип авто"
        verbose_name_plural = "Типы автомобиля"


class TypeLoading(models.Model):
    """
    Класс тип погрузки
    """

    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Тип погрузки"
        verbose_name_plural = "Типы погрузки"


class Units(models.Model):
    """
    Класс единицы измерения
    """

    value = models.CharField(max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Ед.изм."
        verbose_name_plural = "Ед.изм."


class Weight(models.Model):
    """
    Класс вес
    """

    minimum = models.IntegerField(default=1)
    maximum = models.IntegerField(default=10)
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.minimum

    class Meta:
        verbose_name = "Вес"
        verbose_name_plural = "Вес"


class Volume(models.Model):
    """
    Класс объём
    """

    width = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    length = models.IntegerField(default=1)
    unit = models.ForeignKey(Units, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.width

    class Meta:
        verbose_name = "Объём"
        verbose_name_plural = "Объёмы"


class ParametresTrailer(models.Model):
    """
    Класс параметры прицепа
    """

    heightNoLess = models.IntegerField(default=1)
    lackOfSmell = models.BooleanField(default=False)
    lackOfThings = models.BooleanField(default=False)
    woodenFloor = models.BooleanField(default=False)
    dopple = models.BooleanField(default=False)
    demin = models.IntegerField(default=1)
    connik = models.IntegerField(default=1)

    def __str__(self):
        return self.heightNoLess

    class Meta:
        verbose_name = "Параметр прицепа"
        verbose_name_plural = "Параметры прицепа"


class LocationCoordinatesStatus(models.Model):
    """
    Класс статус координат местоположения
    """

    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус координата"
        verbose_name_plural = "Статусы координат"


class LocationCargo(models.Model):
    """
    Класс местоположения груза
    """

    locationCoordinates = models.CharField(max_length=255)
    sendingTimeCoordinates = models.TextField()
    locationCoordinatesStatus = models.ForeignKey(LocationCoordinatesStatus, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.locationCoordinates

    class Meta:
        verbose_name = "Местоположение груза"
        verbose_name_plural = "Местоположения грузов"


class DealStatus(models.Model):
    """
    Класс Статус сделки
    """

    new = models.BooleanField(default=False)
    concluded = models.BooleanField(default=False)
    loading = models.BooleanField(default=False)
    transportation = models.BooleanField(default=False)
    unloading = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.new

    class Meta:
        verbose_name = "Статус сделки"
        verbose_name_plural = "Статусы сделок"


class Deal(models.Model):
    """
    Класс сделка
    """

    numberDealFromClient = models.CharField(max_length=50)
    priceClient = models.IntegerField(default=0)
    companyProfit = models.IntegerField(default=0)
    fromDeal = models.CharField(max_length=255)
    toDeal = models.CharField(max_length=255)
    dateLoading = models.DateTimeField()
    dateUnloading = models.DateTimeField()
    autoReleaseYear = models.IntegerField()
    countPallet = models.IntegerField()
    stateAwning = models.CharField(max_length=100)
    requirementsLoading = models.CharField(max_length=100)
    typeAuto = models.ForeignKey(TypeAuto, on_delete=models.SET_NULL, null=True)
    typeLoading = models.ForeignKey(TypeLoading, on_delete=models.SET_NULL, null=True)
    typeCargo = models.ForeignKey(TypeCargo,on_delete=models.SET_NULL, null=True)
    subclassHazard = models.ForeignKey(SubclassHazard, on_delete=models.SET_NULL, null=True)
    weight = models.ForeignKey(Weight, on_delete=models.SET_NULL, null=True)
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True)
    dealStatus = models.ForeignKey(DealStatus, on_delete=models.SET_NULL, null=True)
    parametresTrailer = models.ForeignKey(ParametresTrailer, on_delete=models.SET_NULL, null=True)
    locationCargo = models.ForeignKey(LocationCargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.numberDealFromClient


    class Meta:
        verbose_name = "Сделка"
        verbose_name_plural = "Сделки"