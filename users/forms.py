from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordResetForm, AuthenticationForm
from django.forms import ModelForm
from django.utils import timezone

from .models import Member, AccountUser
from .utilities import generate_membership

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
import re

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', help_text='Enter a valid email address', required=True)
    zip_code = forms.CharField(label='Postal Code', min_length=6, max_length=6, help_text='Enter a 6 digit postal code')
    
    class Meta:
        model = AccountUser
        fields = ['email', 'password1', 'password2','street_name','zip_code','unit_number','block_number']
    
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['unit_number'].required = False
        self.fields['block_number'].required = False
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            AccountUser.objects.get(email=email)
        except AccountUser.DoesNotExist:
            return email
        raise forms.ValidationError('Please use another Email, that is already taken')
        
    def clean_unit_number(self):
        unit_number = self.cleaned_data.get('unit_number')
        if unit_number == "#N/A" or unit_number == "":
            return unit_number
            
        r = re.compile('#\d{2}-\d{2,3}')
        if r.match(unit_number) is None:
            raise forms.ValidationError('Please enter valid unit number in this format #01-12 or leave as default #N/A')
        return unit_number

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        member_id = generate_membership()
        while(AccountUser.objects.filter(member_id=member_id)):
            member_id = generate_membership()
        user.member_id = member_id
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
        
class ProfileForm(ModelForm):
    class Meta:
        model = Member
        fields = ["name", "eng_date_of_birth"]
        widgets = {
            'eng_date_of_birth': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        labels = {
            'eng_date_of_birth': 'Date-of-birth (eng)',
            'name': 'Name'
        }
        
    def clean_eng_date_of_birth(self):
        data = self.cleaned_data['eng_date_of_birth']
        if data > timezone.now().date():
            raise forms.ValidationError("'DOB' date cannot be later than today.")
        return data

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())