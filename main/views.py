from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(
        request=request,
        template_name='main/base.html'
    )
    
@login_required
def logoutUser(request):
    logout(request)
    return redirect('homepage')