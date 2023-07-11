from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

from desktop.models import * 

class Statistic(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    compressor = models.ForeignKey('desktop.Compressor', on_delete=models.PROTECT)
    opening_hours = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('compressor', kwargs={'id': self.compressor.id})

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ['-created_date']


class History_request(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('desktop.Room', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Помещение')
    compressor = models.ForeignKey('desktop.Compressor', on_delete=models.PROTECT, verbose_name='Компрессор')
    text_open = models.CharField(max_length=200, null=True, blank=True, verbose_name='Возникшая проблема')
    text_close = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')
    mehanical_assembly = models.BooleanField(default=False, verbose_name='Механический узел')
    mehanical_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    mehanical_assembly_shut = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')
    electrical_assembly = models.BooleanField(default=False, verbose_name='Электрический узел')
    electrical_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    electrical_assembly_shut = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')
    oil_assembly = models.BooleanField(default=False, verbose_name='Масляная система')
    oil_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    oil_assembly_shut = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')
    air_assembly = models.BooleanField(default=False, verbose_name='Воздушная система')
    air_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    air_assembly_shut = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')
    another = models.BooleanField(default=False, verbose_name='Другое')
    another_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    another_shut = models.CharField(max_length=200, null=True, blank=True, verbose_name='Решение проблемы')

    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('request', kwargs={'request': 'request','id': self.compressor.id})

    class Meta:
        verbose_name = 'История заявок'
        verbose_name_plural = 'История заявок'
        ordering = ['-created_date']


class History_inspection(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey('desktop.Room', on_delete=models.PROTECT, null=True, blank=True)
    compressor = models.ForeignKey('desktop.Compressor', on_delete=models.PROTECT)
    all_ok = models.BooleanField(default=False, verbose_name='Все в порядке')
    mehanical_assembly = models.BooleanField(default=False, verbose_name='Механический узел')
    mehanical_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    electrical_assembly = models.BooleanField(default=False, verbose_name='Электрический узел')
    electrical_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    oil_assembly = models.BooleanField(default=False, verbose_name='Масляная система')
    oil_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    air_assembly = models.BooleanField(default=False, verbose_name='Воздушная система')
    air_assembly_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    another = models.BooleanField(default=False, verbose_name='Другое')
    another_text = models.CharField(max_length=200, null=True, blank=True, verbose_name='Описание проблемы')
    created_date = models.DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('history_inspection', kwargs={'history_inspection': 'history_inspection','id': self.compressor.id})

    class Meta:
        verbose_name = 'История осмотра'
        verbose_name_plural = 'История осмотра'
        ordering = ['-created_date']
