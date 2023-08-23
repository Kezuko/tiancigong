from django.http import HttpResponse
from django.shortcuts import render, redirect

def homepage(request):
    return render(
        request=request,
        template_name='main/base.html'
    )