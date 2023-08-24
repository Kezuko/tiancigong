from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('create_profile/', views.createProfile, name='create_profile'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('change_password/', views.changePassword, name='change_password/'),
    path("password_reset/", views.passwordResetRequest, name="password_reset_request"),
    path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
]