from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.models import Member
from users.utilities import get_current_lunar_date
from .forms import OrderForm, AdminForm
from .filters import OrderFilter
from .models import Orders

from docxtpl import DocxTemplate
import datetime

LUNAR_CONVERSION = {
    1: "初一",
    2: "初二",
    3: "初三",
    4: "初四",
    5: "初五",
    6: "初六",
    7: "初七",
    8: "初八",
    9: "初九",
    10: "初十",
    11: "十一",
    12: "十二",
    13: "十三",
    14: "十四",
    15: "十五",
    16: "十六",
    17: "十七",
    18: "十八",
    19: "十九",
    20: "二十",
    21: "廿一",
    22: "廿二",
    23: "廿三",
    24: "廿四",
    25: "廿五",
    26: "廿六",
    27: "廿七",
    28: "廿八",
    29: "廿九",
    30: "三十",
}   

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
            current_lunar_date = get_current_lunar_date()    
            if request.POST.get('action') == "preview":
                response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                if form.cleaned_data.get("order_type") == "安太岁":
                    doc = DocxTemplate('services/templates/docx/antaisui.docx')
                    context = {
                        "unit": request.user.unit_number,
                        "block": request.user.block_number,
                        "name": form.cleaned_data.get('member_name'),
                        "day": LUNAR_CONVERSION[current_lunar_date]
                    }
                    response["Content-Disposition"] = 'filename="ats' + str(datetime.datetime.now()) + '.docx"'
                elif form.cleaned_data.get("order_type") == "拜孔子":
                    doc = DocxTemplate('services/templates/docx/antaisui.docx')
                    context = {
                        "unit": request.user.unit_number,
                        "block": request.user.block_number,
                        "name": form.cleaned_data.get('member_name'),
                        "day": LUNAR_CONVERSION[current_lunar_date]
                    }
                    response["Content-Disposition"] = 'filename="bkz' + str(datetime.datetime.now()) + '.docx"'
                elif form.cleaned_data.get("order_type") == "补财库":
                    doc = DocxTemplate('services/templates/docx/pucaiku.docx')
                    context = {
                        "unit": request.user.unit_number,
                        "block": request.user.block_number,
                        "name": form.cleaned_data.get('member_name'),
                        "day": LUNAR_CONVERSION[current_lunar_date]
                    }
                    
                elif form.cleaned_data.get("order_type") == "补运":
                    doc = DocxTemplate('services/templates/docx/puyun.docx')
                    context = {
                        "unit": request.user.unit_number,
                        "block": request.user.block_number,
                        "name": form.cleaned_data.get('member_name'),
                        "day": LUNAR_CONVERSION[current_lunar_date],
                        "newline": "\n"
                    }
                    response["Content-Disposition"] = 'filename="py' + str(datetime.datetime.now()) + '.docx"'
                doc.render(context)
                doc.save(response)
                
                return response
            else:
                order = Orders.objects.filter(order_number=form.cleaned_data['order_number']).update(status="Completed")
                return redirect('order_search')
                
                
                
    