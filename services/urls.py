from django.urls import path
from . import views

urlpatterns = [
    path("services/", views.services, name='services'),
    path("order_search/", views.orderSearch, name='order_search'),
    path("render_document/", views.renderDocument, name='render_document')
]