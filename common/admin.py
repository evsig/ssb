from django.contrib import admin

# Register your models here.
from .models import Audio,Video,Event,Article,Image,Gallery

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass

