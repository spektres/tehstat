from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone

from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .forms import *
from desktop.models import * 
from desktop.utils import *

#Главная страница сервиса
class ServiceHome(LoginRequiredMixin, DataMixin, ListView):
    model = Compressor
    template_name = 'service/service.html'
    context_object_name = 'compressors'
    login_url = reverse_lazy('login') #Перенапр. для неавториз.

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Сервис')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    """def get_queryset(self):
                	return Compressor.objects.filter(room = 2)"""

"""def service(request):
    #Главная страница сервиса
    compressors = Compressor.objects.all().order_by('api')

    context = {
        'compressors': compressors,
        'menu': menu,
        'title': 'Сервис'
    }

    return render(request, 'service/service.html', context=context)"""

#Страница компрессора
class CompressorDetail(LoginRequiredMixin, DetailView):
    model = Compressor
    template_name = 'service/compressor.html'
    pk_url_kwarg = 'id'
    context_object_name = 'posts'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Компрессор'
        return context
		

"""def compressor(request, compressor="", id=""):
    #Страница компрессора
    posts = Compressor.objects.get(id = id)

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'О компрессоре'
    }

    return render(request, 'service/compressor.html', context=context)"""


@login_required
def history(request, id=""):
    #Страница истории компрессора
    posts = History_request.objects.filter(compressor = id)
    compressor = Compressor.objects.get(id = id)

    context = {
        'posts': posts,
        'compressor': compressor,
        'menu': menu,
        'title': 'Истории'
    }

    return render(request, 'service/history.html', context=context)


@login_required
def history_request(request, id=""):
    #Страница истории заявок компрессора
    posts = History_request.objects.filter(compressor = id).order_by('-created_date')
    compressor = Compressor.objects.get(id = id)

    context = {
        'posts': posts,
        'compressor': compressor,
        'menu': menu,
        'title': 'Истории заявок'
    }

    return render(request, 'service/history_request.html', context=context)


@login_required
def history_request_post(request, id="", id_post=""):
    posts = History_request.objects.get(id = id_post)
    compressor = Compressor.objects.get(id = posts.compressor_id)

    context = {
        'posts': posts,
        'compressor': compressor,
        'menu': menu,
        'title': 'Заявка на обслуживание компрессора'
        }

    return render(request, 'service/history_request_post.html', context=context)


"""class RequestShut(UpdateView):
    model = History_request
    template_name = 'service/request_shut.html'
    success_url = reverse_lazy('desktop')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.status = False
        fields.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compressor'] = self.request.GET.get(pk)
        context['menu'] = menu
        context['title'] = 'Закрытие заявки'
        return context"""


@login_required
def history_inspection(request, id=""):
    #Страница истории осмотров компрессора
    posts = History_inspection.objects.filter(compressor = id).order_by('-created_date')
    compressor = Compressor.objects.get(id = id)

    context = {
        'posts': posts,
        'compressor': compressor,
        'menu': menu,
        'title': 'Истории осмотров'
    }

    return render(request, 'service/history_inspection.html', context=context)


@login_required
def history_inspection_post(request, id="", id_post=""):
    #Страница истории осмотров компрессора
    """posts = History_inspection.objects.filter(compressor = id).order_by('-created_date')
                compressor = Compressor.objects.get(id = id)
            
                context = {
                    'posts': posts,
                    'compressor': compressor,
                    'menu': menu,
                    'title': 'Истории осмотра компрессора'
                }"""

    return render(request, 'service/history_inspection_post.html')#, context=context)


"""def add_inspection(request, id=""):
    #Добавление новой записи осмотра компрессора
    return render(request, 'service/add_inspection.html')#, context=context)"""


@login_required
def statistic(request, id=""):
    #Страница статистики компрессора
    posts = Statistic.objects.filter(compressor=id)
    compressor = Compressor.objects.get(id = id)

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'compressor': compressor,
        'menu': menu,
        'title': 'Статистика',
        'page_obj': page_obj
    }

    return render(request, 'service/statistic.html', context=context)

#Страница добавления записи статистики компрессора
"""class StatisticAdd(CreateView):
    form_class = AddStatisticForm
    template_name = 'service/add_statistic.html'
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Обновить статистику'
        return context"""


@login_required
def add_statistic(request, id=""):
    #Страница добавления записи статистики компрессора
    if request.method =='POST':
        form = AddStatisticForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.compressor_id = id
            post.save()
            return redirect('statistic', id)
            #return redirect('statistic', pk=post.pk) - для страницы поста статистики
    else:
        form = AddStatisticForm()

    context = {
        'form': form,
        'menu': menu,
        'title': 'Обновление статистики'
    }

    return render(request, 'service/add_statistic.html', context=context)


@login_required
def request_shut(request, id="", id_post=""):
    posts = History_request.objects.get(id = id_post)
    compressor = Compressor.objects.get(id= posts.compressor_id)

    form = ShutRequestService()

    context = {
        'posts': posts,
        'form': form,
        'compressor': compressor,
        'menu': menu,
        'title': 'Закрыть заявку',
    }

    return render(request, 'service/request_shut.html', context=context)


@login_required
def add_inspection(request, id=""):
    #Страница добавления записи истории осмотра компрессора
    compressor = Compressor.objects.get(id = id)

    if request.method =='POST':
        if 'all_ok' in request.POST:
            form = AddInspectionForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.compressor_id = id
                post.all_ok = True
                post.save()
                return redirect('compressor', id)
        else:
            form = AddInspectionForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                if (post.mehanical_assembly or post.electrical_assembly or post.oil_assembly or post.air_assembly or post.another) == False:
                    form = AddInspectionForm()
                else:
                    if not(post.mehanical_assembly): post.mehanical_assembly_text = ''
                    if not(post.electrical_assembly): post.electrical_assembly_text = ''
                    if not(post.oil_assembly): post.oil_assembly_text = ''
                    if not(post.air_assembly): post.air_assembly_text = ''
                    if not(post.another): post.another_text = ''
                    post.author = request.user
                    post.compressor_id = id
                    post.save()
                    return redirect('compressor', id)
    else:
        form = AddInspectionForm()

    context = {
        'compressor': compressor,
        'form': form,
        'menu': menu,
        'title': 'Осмотр компрессора'
    }

    return render(request, 'service/add_inspection.html', context=context)


"""class AddInspectionService(DataMixin, CreateView):
    model = History_inspection
    form_class = AddInspectionForm
    template_name = 'service/add_inspection_form.html'
    success_url = reverse_lazy('service')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.status = True
        form.save()
        return super(AddRequest, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Подать заявку')
        context = dict(list(context.items()) + list(c_def.items()))
        return context"""

@login_required
def inventory(request):
	#Страница инвентаря
    return HttpResponse('Страница инвентаря')