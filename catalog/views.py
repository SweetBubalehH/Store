from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic 
from django.utils import timezone


def catalog(request):
     template_name='catalog/catalog.html'
     return render(request,template_name)
