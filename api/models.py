from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Hologram(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.TextField(max_length=250, blank=True, null=True)
	picture = models.ImageField(upload_to='pictures', blank=True)
	created = models.DateTimeField(auto_now_add=True)
	to_update = models.DateTimeField(auto_now=True)

	class meta:
 		ordering = ('-to_update',)
 		
	def __str__(self):
	    return self.name 	