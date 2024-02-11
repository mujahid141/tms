from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("ok")

# Create your views here.
