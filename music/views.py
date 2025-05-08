from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(_request):
    return HttpResponse("My first API!")
