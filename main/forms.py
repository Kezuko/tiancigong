from django import forms
from users.models import AccountUser

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email", help_text='Enter a valid email address', required=True)
    zip_code = forms.CharField(label='Postal Code', min_length=6, max_length=6, help_text='Enter a 6 digit postal code')
    
    class Meta:
        model = AccountUser
        exclude = ['member_id','username','address','is_staff','is_active','is_superuser','created_date','modified_date']
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user