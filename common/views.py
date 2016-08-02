# coding: utf-8
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView


class StaticPageView(TemplateView):
    """Выдаёт статические страницы.
    Имя шаблона статической страницы совпадает с именем в URL.
    Если шаблона нет, то выдаётся 404.
    """
    def dispatch(self, request, *args, **kwargs):
        """Определяет имя шаблона и вызывает стандартный dispatch.
        """
        name = kwargs.get('template_name', '').strip()
        self.template_name = name
        try:
            response = super(StaticPageView, self).dispatch(request, *args,
                                                             **kwargs)
            return response.render()
        except TemplateDoesNotExist:
            raise Http404