from django.contrib.auth.backends import BaseBackend
from .models import Police

class PoliceAuthBackend(BaseBackend):
    def authenticate(self, request, police_email=None, password=None, **kwargs):
        try:
            user = Police.objects.get_by_natural_key(police_email)
            if user.check_password(password):
                return user
        except Police.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Police.objects.get(pk=user_id)
        except Police.DoesNotExist:
            return None
