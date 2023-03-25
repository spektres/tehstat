from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.utils import timezone

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .utils import * 
from service.models import * 
from .forms import *

#Главная страница рабочего стола
def desktop(request):
    requests_true = History_request.objects.filter(status=True).order_by('-created_date')
    requests_false = History_request.objects.filter(status=False).order_by('-created_date')

    context = {
        'requests_true': requests_true,
        'requests_false': requests_false,
        'menu': menu,
        'title': 'Рабочий стол'
    }

    return render(request, 'desktop/desktop.html', context=context)

#Регистрация пользователя
class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'desktop/register.html'
    success_url = reverse_lazy('service')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    #Автоматическая авторизация при регистрации
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('service')
		
#Авторизация
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'desktop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    def get_success_url(self):
    	return reverse_lazy('service')

#Выход из аккаунта
def logout_user(request):
    logout(request)
    return redirect('login')

#Создание заявки (Выполнить декорацию!!!!)
class AddRequest(DataMixin, CreateView):
    model = History_request
    form_class = RequestForm
    template_name = 'desktop/request_form.html'
    success_url = reverse_lazy('desktop')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = True
        form.save()
        return super(AddRequest, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Подать заявку')
        context = dict(list(context.items()) + list(c_def.items()))
        return context
#Подгрузка списка компрессоров для заявок
def load_compressors(request):
    room_id = request.GET.get('room')
    compressors = Compressor.objects.filter(room_id=room_id)
    return render(request, 'desktop/compressor_dropdown_list_options.html', {'compressors': compressors})


# !!!!Нужно запретить изменение заявки, если она не активна
"""class RequestShut(UpdateView):
    model = History_request
    pk_url_kwarg = 'id'
    template_name = 'desktop/request_shut.html'
    fields = ['text_close']
    success_url = reverse_lazy('desktop')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.status = False
        fields.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Закрытие заявки'
        return context"""