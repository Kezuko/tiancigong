from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from .managers import AccountUserManager
from .utilities import generate_membership

class AccountUser(AbstractBaseUser, PermissionsMixin):
    username = None
    member_id = models.CharField(primary_key=True, default=generate_membership, editable=False, max_length=18)
    email = models.EmailField(null=False, blank=False, unique=True)
    zip_code = models.CharField(max_length=6,null=False, blank=False)
    street_name = models.CharField(max_length=500, null=False, blank=False)
    block_number = models.CharField(max_length=10)
    unit_number = models.CharField(max_length=40, default='#')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    
    REQUIRED_FIELDS = ['password','street_name','zip_code']
    USERNAME_FIELD = 'email'
    
    objects = AccountUserManager()
    
    def __str__(self):
        return self.member_id
    
class Member(models.Model):
    account = models.ForeignKey('AccountUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=False, blank=False)
    eng_date_of_birth = models.DateField(null=False, blank=False)
    chi_date_of_birth = models.DateField(null=False, blank=False)
    zodiac = models.CharField(null=False, blank=False, max_length=50)
    
    def __str__(self):
        return self.name