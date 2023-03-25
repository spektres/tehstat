from django import forms
from .models import *
from service.models import * 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class RequestForm(forms.ModelForm):
    class Meta:
        model = History_request
        fields = ('room', 'compressor', 'mehanical_assembly', 'mehanical_assembly_text', 'electrical_assembly', 'electrical_assembly_text', 'oil_assembly', 'oil_assembly_text', 'air_assembly', 'air_assembly_text', 'another', 'another_text', 'text_open')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['compressor'].queryset = Compressor.objects.none()

        if 'room' in self.data:
            try:
                room_id = int(self.data.get('room'))
                self.fields['compressor'].queryset = Compressor.objects.filter(room_id=room_id).order_by('api')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['compressor'].queryset = self.instance.room.compressor_set.order_by('api')
