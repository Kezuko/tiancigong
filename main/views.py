from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return HttpResponse("This is our homepage It works!")