from service.models import * 
from .models import *

menu = [{'title': 'Рабочий стол', 'url_name': 'desktop'},
    {'title': 'Сервис', 'url_name': 'service'},
    {'title': 'Инвентарь', 'url_name': 'inventory'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        compressors = Compressor.objects.all()
        context['menu'] = menu
        context['compressors'] = compressors
        return context