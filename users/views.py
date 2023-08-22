from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

#Custom Imports
from .decorators import user_not_authenticated
from .forms import UserRegistrationForm, ProfileForm
from .tokens import account_activation_token

#For Email
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

from geopy.geocoders import Nominatim

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")
        
    return redirect('homepage')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("activate_account_email_template.html", {
        'member_id': user.member_id,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])

    if email.send():
        messages.success(request, f'Please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

@user_not_authenticated
def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data["username"],
                password = form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Hello <b>{user.email}</b>! You have been logged in.')
                return redirect("create_profile")
        else:
            for error in list(form.errors.values()):
                 messages.error(request, error)
               
    form = AuthenticationForm()
        
    return render(
        request=request,
        template_name="users/login.html",
        context={"form": form}
    )
    
@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            geolocator = Nominatim(user_agent="geoapiExercises")
            address = geolocator.geocode(form.cleaned_data["zip_code"])
            user = form.save(commit=False)
            user.is_active=False
            user.address = address
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('homepage')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name = "users/register.html",
        context={"form": form}
    )
     
@login_required
def createProfile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = request.user
            profile.save()
            return redirect('homepage')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name = "users/createprofile.html",
        context={"form": form}
    )
    return redirect('homepage')
     
@login_required
def logoutUser(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('homepage')

