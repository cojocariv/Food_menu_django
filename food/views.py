from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('dsfd')

def item(request):
    return HttpResponse('<h1>this is a item</h1>')