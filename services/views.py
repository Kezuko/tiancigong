from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import Member
from .forms import OrderForm, AdminForm
from .filters import OrderFilter
from .models import Orders

from docxtpl import DocxTemplate
import datetime

@login_required
def services(request):
    if request.method == "POST":
        form = OrderForm(request=request, data=request.POST)
        if form.is_valid():
            order = form.save()
            messages.success(request, "Order Submitted!")
        else:
            for key, error in list(form.errors.items()):
                messages.error(request, error)
    else:
        form = OrderForm(request)
    return render(
        request=request,
        template_name = "services/services.html",
        context={"form": form,
            "member_id": request.user.member_id
        }
    )
    
@login_required
def orderSearch(request):
    orders = Orders.objects.all()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    return render(
        request=request,
        template_name = "services/orderSearch.html",
        context={
            "orders": orders,
            "myFilter": myFilter
        }
    )
    

def renderDocument(request):
    if request.method == "POST":
        form = AdminForm(request=request, data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get("order_type") == "拜孔子":
                doc = DocxTemplate('services/templates/docx/baikongzi.docx')
                context = {
                    "name": form.cleaned_data.get('member_name')
                }
    #doc = DocxTemplate('services/templates/docx/taisui.docx')
    
    
    
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    response["Content-Disposition"] = 'filename="your_doc_name' + str(datetime.datetime.now()) + '.docx"'
    doc.render(context)
    doc.save(response)
    
    return response