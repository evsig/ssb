# coding: utf-8
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Audio,Video,Event,Article,Image,Gallery


class StaticPageView(TemplateView):
    """Выдаёт статические страницы.
    Имя шаблона статической страницы совпадает с именем в URL.
    Если шаблона нет, то выдаётся 404.
    """
    def dispatch(self, request, *args, **kwargs):
        """Определяет имя шаблона и вызывает стандартный dispatch.
        """
        name = kwargs.get('template_name', '').strip()
        print kwargs
        self.template_name = name
        try:
            response = super(StaticPageView, self).dispatch(request, *args,
                                                             **kwargs)
            return response.render()
        except TemplateDoesNotExist:
            raise Http404


class AudioListView(ListView):
    model = Audio
    template_name = "audio/list.html"

class AudioDetailView(DetailView):
    model = Audio
    template_name = "audio/item.html"


class VideoListView(ListView):
    model = Video
    template_name = "video/list.html"

class VideoDetailView(DetailView):
    model = Video
    template_name = "video/item.html"



class EventListView(ListView):
    model = Event
    template_name = "event/list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "event/item.html"


class ArticleListView(ListView):
    model = Article
    template_name = "article/list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/item.html"


class GalleryListView(ListView):
    model = Gallery
    template_name = "gallery/list.html"

class GalleryDetailView(DetailView):
    model = Gallery
    template_name = "gallery/item.html"