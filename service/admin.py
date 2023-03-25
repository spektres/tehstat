from django.contrib import admin

from . models import Statistic, History_request, History_inspection
admin.site.register(Statistic)
admin.site.register(History_request)
admin.site.register(History_inspection)