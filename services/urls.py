from django.urls import path
from . import views

urlpatterns = [
    path("<eng_name>/services/", views.services, name='services')
]