from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class Citizen(AbstractBaseUser):
    citizen_id = models.AutoField(primary_key=True)
    citizen_fname = models.CharField(max_length=100, null=False, blank=False)
    citizen_email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    citizen_phno = models.CharField(max_length=10, null=False, blank=False, unique=True)
    citzen_state = models.CharField(max_length=100, null=False, blank=False)
    citizen_city = models.CharField(max_length=100, null=False, blank=False)
    citizen_locality = models.CharField(max_length=100, null=False, blank=False)
    citizen_dob = models.DateField(null=False, blank=False)
    citizen_address = models.CharField(max_length=100, null=False, blank=False)
    citizen_pincode = models.CharField(max_length=6, null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = ["citizen_phno", "citizen_email"]
    REQUIRED_FIELDS = ["citizen_fname", "citizen_address", "citizen_city", "citizen_pincode", "citizen_dob"]
    
    def __str__(self):
        return self.citizen_id
    