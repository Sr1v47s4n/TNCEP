from django.contrib.auth.models import BaseUserManager

class PoliceManager(BaseUserManager):
    def create_user(self, police_id, police_name, police_email, police_phno, police_city, police_locality, police_post, password=None, **extra_fields):
        if not police_email:
            raise ValueError('The Police ID must be set')
        if not police_phno:
            raise ValueError('The Police Phone number must be set')

        user = self.model(
            police_id=police_id,
            police_name=police_name,
            police_email=self.normalize_email(police_email),
            police_phno=police_phno,
            police_city=police_city,
            police_locality=police_locality,
            police_post=police_post,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, police_id, police_name, police_email, police_phno, police_city, police_locality, police_post, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(police_id, police_name, police_email, police_phno, police_city, police_locality, police_post, password, **extra_fields)
