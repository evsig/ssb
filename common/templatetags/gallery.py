from django import template

register = template.Library()
from ..models import Image

@register.simple_tag(takes_context=True)
def get_random_gallery(context):
	context['random_images'] = Image.objects.order_by('?')[:10]
	return '';