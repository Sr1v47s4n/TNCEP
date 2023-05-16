from django.contrib.auth.backends import ModelBackend
from .models import Citizen

class CitizenBackend(ModelBackend):
    def authenticate(self, request, citizen_aadhaar=None, password=None, **kwargs):
        try:
            citizen = Citizen.objects.get(citizen_aadhaar=citizen_aadhaar)
        except Citizen.DoesNotExist:
            return None

        if citizen.check_password(password):
            return citizen

    def get_user(self, user_id):
        try:
            return Citizen.objects.get(pk=user_id)
        except Citizen.DoesNotExist:
            return None
