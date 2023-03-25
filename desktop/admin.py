from django.contrib import admin

from . models import Compressor, Compressor_type, Compressor_model, Compressor_lable, Room, Company
admin.site.register(Compressor)
admin.site.register(Compressor_type)
admin.site.register(Compressor_model)
admin.site.register(Compressor_lable)
admin.site.register(Room)
admin.site.register(Company)