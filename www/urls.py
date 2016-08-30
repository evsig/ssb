"""www URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from common.views import StaticPageView, GalleryListView, GalleryDetailView, AudioListView, AudioDetailView, VideoListView, VideoDetailView, ArticleListView, ArticleDetailView, EventListView, EventDetailView

admin.autodiscover()

urlpatterns = []

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    
    url(r'^admin/', admin.site.urls),

    #generic views
    url(r'^gallery/$', GalleryListView.as_view(), name='gallery-list'),
    url(r'^gallery/(?P<pk>\d+)/$', GalleryDetailView.as_view(), name='gallery-detail'),

    url(r'^audio/$', AudioListView.as_view(), name='audio-list'),
    url(r'^audio/(?P<pk>\d+)/$', AudioDetailView.as_view(), name='audio-detail'),

    url(r'^video/$', VideoListView.as_view(), name='video-list'),
    url(r'^video/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),

    url(r'^article/$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article-detail'),

    url(r'^event/$', EventListView.as_view(), name='event-list'),
    url(r'^event/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-detail'),

    # static page resolve
    url(r'^$', StaticPageView.as_view(), kwargs={ 'template_name' : 'index.html' }),
    url(r'^(?P<template_name>.*)$', StaticPageView.as_view(), name='page'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
