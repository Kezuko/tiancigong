from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create_profile/', views.createProfile, name='create_profile'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
    
]