from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import Member
from .forms import OrderForm

@login_required
def services(request):
    if request.method == "POST":
        form = OrderForm(data=request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, "Order Submitted!")
        else:
            for key, error in list(form.errors.items()):
                messages.error(request, error)
    else:
        form = OrderForm()
    return render(
        request=request,
        template_name = "services/services.html",
        context={"form": form,
            "member_id": request.user.member_id
        }
    )
    
    
   