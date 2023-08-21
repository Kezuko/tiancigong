from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .decorators import user_not_authenticated

@user_not_authenticated
def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("homepage")
        else:
            for error in list(form.errors.values()):
                 messages.error(request, error)
               
    form = AuthenticationForm()
        
    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )
    
@user_not_authenticated
def register(request):
    pass
             
@login_required
def logoutUser(request):
    logout(request)
    return redirect('homepage')

