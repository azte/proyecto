from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from django.shortcuts import render_to_response
from models import *

def home(request):
	categorias = Categoria.objects.all()
	enlaces = Enlace.objects.all()
	template = "index.html"
	#diccionario = {"categorias":categorias,"enlaces":enlaces} En lugar de locals
	return render_to_response(template,locals())





##### USO DE SHORTCUT #####

def hora_actual(request):
	now = datetime.now()
	return render_to_response('hora.html', {'hora':now,"usuario":"Carlangas"})



##### MODO LARGO SIN SHORTCUT #####
	#def hora_actual(request):
	# ahora = datetime.now()
	# t = get_template("hora.html")
	# c = Context({"hora":ahora,"usuario":"Carlitos"})
	# html = t.render(c)
	# return HttpResponse(html)
