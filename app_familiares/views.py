from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context, loader
from app_familiares.models import familiar


# Create your views here.

def probar_template(request):
    queryset = familiar.objects.all()
    diccionario = {'familiares': queryset}
    plantilla = loader.get_template('plantilla_familiares.html')
    documento_html = plantilla.render(diccionario)
    
    return HttpResponse(documento_html)