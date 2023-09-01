from django import forms
from django.forms import ModelForm
from .models import Orders
from users.models import Member, AccountUser
from users.utilities import generate_membership

class OrderForm(ModelForm):
    member_id = forms.CharField(max_length=36)
    member_name = forms.MultipleChoiceField(choices=(),required=True)
    
    def __init__(self, request, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        members = Member.objects.filter(account=request.user)
        mem = []
        for member in members:
            mem.append((getattr(member, 'name'),getattr(member, 'name')))
        self.fields['member_name'].choices = mem
    
    class Meta:
        model = Orders
        fields = ['order_type']
    
    def save(self, commit=True):
        order_prefix = {
            '补运': 'PY',
            '补财库': 'PQK',
            '拜孔子': 'PKZ',
            '安太岁': 'ATS',
            '接财神': 'BCS',
            '拜天狗': 'BTG',
            '拜無鬼': 'BWG',
            '拜天宫': 'BTG'
        }
        cleaned_data = self.cleaned_data 
        order = super(OrderForm, self).save(commit=False)
        order.account = AccountUser.objects.get(member_id=self.cleaned_data['member_id'])       
        order_id = '{}{}'.format(order_prefix[cleaned_data['order_type']],generate_membership())
        while(Orders.objects.filter(order_number=order_id)):
            order_id = '{}{}'.format(order_prefix[cleaned_data['order_type']],generate_membership())
        order.order_number = order_id
        if commit:
            order.save()
            for name in cleaned_data['member_name']:
                order.member.add(Member.objects.get(account__member_id=cleaned_data['member_id'], name=name))
        return order

        