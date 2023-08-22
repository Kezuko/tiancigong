from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.utils import timezone

from .models import Member
from .models import AccountUser

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email', help_text='Enter a valid email address', required=True)
    zip_code = forms.CharField(label='Postal Code', min_length=6, max_length=6, help_text='Enter a 6 digit postal code')
    
    class Meta:
        model = AccountUser
        fields = ['email', 'password1', 'password2', 'zip_code']
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            AccountUser.objects.get(email=email)
        except AccountUser.DoesNotExist:
            return email
        raise forms.ValidationError('Please use another Email, that is already taken')  
     
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
        
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

        