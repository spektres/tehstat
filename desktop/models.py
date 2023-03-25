from django.conf import settings
from django.db import models
from django.utils import timezone

from service.models import *

class Company(models.Model):
    company = models.CharField(max_length=200)

    def __str__(self):
        return str(self.company)

class Room(models.Model):
    company = models.ForeignKey('Company', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Compressor_lable(models.Model):
    name = models.CharField(max_length=200, unique=True)
    manufacturer = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Compressor_model(models.Model):
    compressor_lable = models.ForeignKey('Compressor_lable', on_delete=models.PROTECT)
    compressor_type = models.ForeignKey('Compressor_type', on_delete=models.PROTECT)
    name = models.CharField(max_length=50, unique=True)
    drive = models.CharField(max_length=50)
    nutrition = models.CharField(max_length=50)
    cooling = models.CharField(max_length=50)
    max_turnover = models.IntegerField()
    min_turnover = models.IntegerField()
    noise_level = models.IntegerField()
    tank_oil = models.IntegerField()
    effeciency = models.IntegerField()
    max_pressure = models.IntegerField()
    engine_power = models.IntegerField()
    #Перечислить характеристики

    def __str__(self):
        return str(self.name)

class Compressor_type(models.Model):
    TYPE_NAMES = (
        ('Винтовой', 'screw'),
        ('Поршневой', 'piston'),
        ('Спиральный', 'spiral'),
    )
    type_name = models.CharField(max_length=50, choices=TYPE_NAMES)

    def __str__(self):
        return str(self.type_name)
        

class Compressor(models.Model):
    compressor_model = models.ForeignKey('Compressor_model', on_delete=models.PROTECT)
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    api = models.IntegerField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)

    def __str__(self):
        return str(self.api)

    def get_absolute_url(self):
        return reverse('compressor', kwargs={'id': self.id})



