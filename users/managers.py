from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from geopy.geocoders import Nominatim

class AccountUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
            
        if not extra_fields.get('zip_code'):
            raise ValueError('Users require a postal code')
            
        if not extra_fields.get('address'):
            raise ValueError('Users require an address')
        
        if not extra_fields.get('unit_number'):
            raise ValueError('Users require a unit number')
            
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)
        return self._create_user(email, password, **extra_fields)
        
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have sufficient privilege')
        
        return self._create_user(email, password, **extra_fields)
        