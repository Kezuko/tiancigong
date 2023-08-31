from django import forms
from django.forms import ModelForm
from .models import Orders
from users.models import Member, AccountUser

class OrderForm(ModelForm):
    member_id = forms.CharField(max_length=36)
    member_eng_name = forms.CharField(max_length=100)
    
    class Meta:
        model = Orders
        fields = ['order_type']

    def clean(self):
        cleaned_data = self.cleaned_data 
        orders = Orders.objects.filter(account__member_id=cleaned_data['member_id'], member__eng_name=cleaned_data['member_eng_name'], order_type=cleaned_data['order_type'])

        if orders:
            raise forms.ValidationError('Order already exists.')  
        return cleaned_data
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data 
        order = super(OrderForm, self).save(commit=False)
        order.account = AccountUser.objects.get(member_id=self.cleaned_data['member_id'])
        order.member = Member.objects.get(account__member_id=cleaned_data['member_id'], eng_name=self.cleaned_data['member_eng_name'])
        if commit:
            order.save()
        return order

        