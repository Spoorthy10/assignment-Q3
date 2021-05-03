from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sample(request):
    return HttpResponse("this is sample function of multiple application")

def hello(request):
    return HttpResponse("this is hello function of multiple application")

def test(request):
    return HttpResponse('<h1> this is test function of multiple application <h1>')

def method(request):
    return HttpResponse('<marquee><h1>this is method function of multiple application<h1><marquee>')
