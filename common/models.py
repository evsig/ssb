from __future__ import unicode_literals

from django.db import models

from sorl.thumbnail import ImageField

# Create your models here.
class CommonMedia(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now_add=True)
	description = models.TextField()

	def __unicode__(self):
		return self.title

class Audio(CommonMedia):
	iframe_data = models.TextField(max_length=500)

class Video(CommonMedia):
	iframe_data = models.TextField(max_length=500)

class Image(CommonMedia):
	file = ImageField(upload_to='image/%Y/%m/%d')

class Gallery(CommonMedia):
	images = models.ManyToManyField(Image)


class Article(CommonMedia):
	pass

class Event(CommonMedia):
	audios = models.ManyToManyField(Audio)
	videos = models.ManyToManyField(Video)
	gallery = models.ManyToManyField(Gallery)
	texts = models.ManyToManyField(Article)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)