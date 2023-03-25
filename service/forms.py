from django import forms
from .models import *
from desktop.models import * 

class AddStatisticForm(forms.ModelForm):
    class Meta:
        model = Statistic
        fields =  ['opening_hours', 'number_of_starts', 'load_relay', 'fan_starts', 'accumulated_volume', 'regulator_hours']

class ShutRequestService(forms.ModelForm):
    class Meta:
        model = History_request
        fields = ('room', 'compressor', 'mehanical_assembly', 'mehanical_assembly_text', 'mehanical_assembly_shut', 'electrical_assembly', 'electrical_assembly_text', 'oil_assembly', 'oil_assembly_text', 'air_assembly', 'air_assembly_text', 'another', 'another_text', 'text_open')
        """widgets = {
                                    'mehanical_assembly': forms.TextInput(attrs={'class': 'add_mehanical_assembly'})
                                }"""

"""class AddInspectionForm(forms.Form):
    #all_ok = forms.BooleanField(label='Все в норме')
    mehanical_assembly = forms.BooleanField(label='Механический узел')
    mehanical_assembly_text = forms.CharField(label='Описание проблемы')
    electrical_assembly = forms.BooleanField(label='Электричский узел')
    electrical_assembly_text = forms.CharField(label='Описание проблемы')
    oil_assembly = forms.BooleanField(label='Масляная система')
    oil_assembly_text = forms.CharField(label='Описание проблемы')
    air_assembly = forms.BooleanField(label='Воздушная система')
    air_assembly_text = forms.CharField(label='Описание проблемы')
    another = forms.BooleanField(label='Другая неисправность')
    another_text = forms.CharField(label='Описание проблемы')"""

class AddInspectionForm(forms.ModelForm):
    class Meta:
        model = History_inspection
        fields = ('mehanical_assembly', 'mehanical_assembly_text', 'electrical_assembly', 'electrical_assembly_text', 'oil_assembly', 'oil_assembly_text', 'air_assembly', 'air_assembly_text', 'another', 'another_text',)


# Пример формы, не связанной с моделью.
"""class AddStatisticForm(forms.Form):
    author = forms.CharField(max_length=50, label="Автор")
    compressor = forms.ModelChoiceField(queryset=Compressor.objects.all())
    opening_hours = forms.IntegerField(label="Часы работы")
    number_of_starts = forms.IntegerField()
    load_relay = forms.IntegerField()
    fan_starts = forms.IntegerField()
    accumulated_volume = forms.IntegerField()
    regulator_hours = forms.IntegerField()"""

    
    # Атрибут required=False делает поле необязательным

		