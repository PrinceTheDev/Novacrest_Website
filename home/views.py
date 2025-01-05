from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Welcome to the Novacrest Hospital')

# Create your views here.
