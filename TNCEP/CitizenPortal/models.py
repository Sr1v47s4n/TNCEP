from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class Citizen(AbstractBaseUser):
    citizen_id = models.AutoField(primary_key=True)
    citizen_fname = models.CharField(max_length=100, null=False, blank=False)
    citizen_email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    citizen_phno = models.CharField(max_length=10, null=False, blank=False, unique=True)
    citizen_aadhar = models.CharField(max_length=10, null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD ="citizen_aadhar"
    REQUIRED_FIELDS = ["citizen_fname","citizen_email","citizen_phno","citizen_fname", ]
    
    def __str__(self):
        return self.citizen_id
    