from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("<eng_name>/services/", views.services, name='services'),
]