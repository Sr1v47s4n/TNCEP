from django.db import models
from django.utils import timezone


class NormalComplaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_type = models.CharField(max_length=50, null=False, blank=False)
    complaint_desc = models.TextField(max_length=500, null=False, blank=False)
    complaint_loc = models.CharField(max_length=150, null=False, blank=False)
    complaint_date = models.DateTimeField(default=timezone.now)
    complaint_status = models.CharField(max_length=50, null=False, blank=False)
    complaint_image = models.ImageField(upload_to="complaints/images", null=True, blank=True)
    complaint_video = models.FileField(upload_to="complaints/videos", null=True, blank=True)
    complaint_citizen = models.ForeignKey("CitizenPortal.Citizen", on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.complaint_id
    
class EmergencyComplaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_type = models.CharField(max_length=50, null=False, blank=False)
    complaint_desc = models.TextField(max_length=500, null=True, blank=True)
    complaint_loc = models.CharField(max_length=150, null=False, blank=False)
    complaint_date = models.DateTimeField(default=timezone.now)
    complaint_status = models.CharField(max_length=50, null=True, blank=True)
    complaint_image = models.ImageField(upload_to="complaints/images", null=True, blank=True)
    complaint_video = models.FileField(upload_to="complaints/videos", null=True, blank=True)

    def __str__(self):
        return self.complaint_id
    
class AnonComplaint(models.Model):
    complaint_id = models.AutoField(primary_key=True)
    complaint_type = models.CharField(max_length=50, null=False, blank=False)
    complaint_desc = models.TextField(max_length=500, null=False, blank=False)
    complaint_loc = models.CharField(max_length=150, null=False, blank=False)
    complaint_date = models.DateTimeField(default=timezone.now)
    complaint_status = models.CharField(max_length=50, null=False, blank=False)
    complaint_image = models.ImageField(upload_to="complaints/images", null=True, blank=True)
    complaint_video = models.FileField(upload_to="complaints/videos", null=True, blank=True)

    def __str__(self):
        return self.complaint_id