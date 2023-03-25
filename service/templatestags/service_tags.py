"""from django import template
from service.models import *
from desktop.models import *

register = template.Library()

@register.simple_tag()
def get_compressor():
	return Compressor.objects.get(id = id)"""