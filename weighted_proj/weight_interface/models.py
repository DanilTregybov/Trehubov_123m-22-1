from django.db import models


# Create your models here.

class CerealCrops(models.Model):
    """
    Таблиця Зернових культур(Отримання)
    """
    Date = models.DateField(auto_now_add=True)  # Дата поставки
    Supplier = models.CharField(max_length=150)  # Постачальник
    Place_of_download = models.CharField(max_length=350)  # Місце завантаження
    Recipient = models.CharField(max_length=150)  # Одержувач
    Delivery_condition = models.CharField(max_length=10)  # Умова поставки
    Analysis_number = models.IntegerField()  # Номер аналізу
    Number_of_CN = models.IntegerField()  # Номер ТТН
    Car_license_plate = models.CharField(max_length=15)  # Реєстраційний номер авто
    Trailer_license_plate = models.CharField(max_length=15)  # Реєстраційний номер причіпа
    Gross_weight_kilos = models.FloatField()  # Вага брутто, кг
    Tare_weight_kilos = models.FloatField()  # Вага тари, кг
    Weight_on_invoice_kilos = models.FloatField()  # Вага по накладній БРУТТО, кг
    Weight_net_kilos = models.FloatField()  # Вага по накладній НЕТТО, кг
    Actual_weight = models.FloatField()  # Вага фактична, кг
    Lack_of = models.FloatField()  # Нестача
    Driver = models.CharField(max_length=80)  # Водій
    Driver_phone = models.CharField(max_length=40)  # Телефон водія
    Carrier = models.CharField(max_length=150)  # Перевізник
    Check_in_time = models.TimeField()  # Час заїзду
    Departure_time = models.TimeField()  # Час виїзду
    Weightman = models.CharField(max_length=80)  # Ваговик


    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}".format(self.pk,self.Date,
                                                                             self.Supplier, self.Place_of_download,
                                                                             self.Recipient, self.Delivery_condition,
                                                                             self.Analysis_number,
                                                                             self.Number_of_CN, self.Car_license_plate,
                                                                             self.Trailer_license_plate,
                                                                             self.Gross_weight_kilos,
                                                                             self.Tare_weight_kilos,
                                                                             self.Weight_on_invoice_kilos,
                                                                             self.Actual_weight, self.Lack_of,
                                                                             self.Driver,
                                                                             self.Driver_phone, self.Carrier,
                                                                             self.Check_in_time, self.Departure_time,
                                                                             self.Weightman)


class LogShippedProducts(models.Model):
    """
    Таблиця Відвантаження готової продукції
    """
    Status = models.BooleanField(default=False)  # Стан
    Date = models.DateTimeField(auto_now_add=True)  # Дата поставки
    Customer = models.CharField(max_length=150)  # Покупець
    Product = models.CharField(max_length=150)  # Продукція
    Current_container = models.CharField(max_length=150)  # Поточна тара
    Tare_weight_kilos = models.FloatField()  # Вага тари, кг
    Net_weight_kilos = models.FloatField()  # Вага нетто, кг
    Price = models.IntegerField()  # Ціна
    Carrier = models.CharField(max_length=150)  # Перевізник
    Driver = models.CharField(max_length=80)  # Водій
    Driver_phone = models.CharField(max_length=40)  # Телефон водія
    Unloading_point = models.CharField(max_length=350)  # Пункт вивантаження
    Car_license_plate = models.CharField(max_length=15)  # Реєстраційний номер авто
    Trailer_license_plate = models.CharField(max_length=15)  # Реєстраційний номер причіпа
    Departure_time = models.TimeField()  # Час виїзду
    Weightman = models.CharField(max_length=80)  # Ваговик

    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.pk,
                                                                      self.Status,
                                                                      self.Date,
                                                                      self.Customer,
                                                                      self.Product,
                                                                      self.Current_container,
                                                                      self.Tare_weight_kilos,
                                                                      self.Net_weight_kilos,
                                                                      self.Price,
                                                                      self.Driver,
                                                                      self.Driver_phone,
                                                                      self.Unloading_point,
                                                                      self.Car_license_plate,
                                                                      self.Trailer_license_plate,
                                                                      self.Departure_time,
                                                                      self.Weightman)


class AuxiliaryMaterials(models.Model):
    """
        Таблиця Допоміжних матеріалів
    """
    Date = models.DateTimeField(auto_now_add=True)  # Дата поставки
    Product_name = models.CharField(max_length=150)  # Продукція
    Supplier = models.CharField(max_length=150)  # Постачальник
    Car_license_plate = models.CharField(max_length=15)  # Реєстраційний номер авто
    Trailer_license_plate = models.CharField(max_length=15)  # Реєстраційний номер причіпа
    Time_1st_weighing = models.TimeField()  # Час 1-го зважування
    Gross_weight_kilos = models.FloatField()  # Вага брутто, кг
    Time_2nd_weighing = models.TimeField()  # Час 2-го зважування
    Tare_weight_kilos = models.FloatField()  # Вага тари, кг
    Net_weight_kilos = models.FloatField()  # Вага нетто, кг
    Weight_on_invoice_kilos = models.FloatField()  # Вага по накладній,кг
    Surplus = models.FloatField()  # Надлишок,кг
    Lack_of = models.FloatField()  # Нестача,кг
    Driver = models.CharField(max_length=80)  # Водій
    Weightman = models.CharField(max_length=80)  # Ваговик
    Number_of_CN = models.IntegerField()  # Номер ТТН

    def __str__(self):
        return "{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.Date,
                                                                      self.Product_name,
                                                                      self.Supplier,
                                                                      self.Car_license_plate,
                                                                      self.Trailer_license_plate,
                                                                      self.Time_1st_weighing,
                                                                      self.Gross_weight_kilos,
                                                                      self.Time_2nd_weighing,
                                                                      self.Tare_weight_kilos,
                                                                      self.Net_weight_kilos,
                                                                      self.Weight_on_invoice_kilos,
                                                                      self.Surplus,
                                                                      self.Lack_of,
                                                                      self.Driver,
                                                                      self.Weightman,
                                                                      self.Number_of_CN, )
