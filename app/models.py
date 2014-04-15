from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
	titulo = models.CharField(max_length=256)

	def __unicode__(self): #Para ver el titulo en el admin y No object
		return self.titulo

class Enlace(models.Model):

	
	titulo = models.CharField(max_length=140)
	enlace = models.URLField()
	votos = models.IntegerField(default=0)
	categoria = models.ForeignKey(Categoria)
	usuario = models.ForeignKey(User)


	def __unicode__(self):
		return "%s - %s" %(self.titulo,self.enlace)

