import django_filters
from django_filters import CharFilter

from .models import Orders

class OrderFilter(django_filters.FilterSet):
    Membership = CharFilter(label='Membership', field_name="account__member_id", lookup_expr='icontains')
    Name = CharFilter(label='Name', field_name="member__name", lookup_expr='icontains')
    
    class Meta:
        model = Orders
        exclude = ['account','member']
        
    