from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from .manager import PoliceManager

class Police(AbstractBaseUser):
    police_id = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    police_name = models.CharField(max_length=100, null=False, blank=False)
    police_email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    police_phno = models.CharField(max_length=10, null=False, blank=False, unique=True)
    police_city = models.CharField(max_length=100, null=False, blank=False)
    police_locality = models.CharField(max_length=100, null=False, blank=False)
    police_post = models.CharField(max_length=100, null=False, blank=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = PoliceManager()
    USERNAME_FIELD = "police_email"
    REQUIRED_FIELDS = ["police_name", "police_id", "police_phno", "police_city", "police_locality", "police_post"]
    
    
    def __str__(self):
        return self.police_id
    
  