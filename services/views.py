from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def services(request, eng_name):
    return render(
        request=request,
        template_name='main/base.html'
    )