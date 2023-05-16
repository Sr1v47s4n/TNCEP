from django.contrib.auth.models import BaseUserManager

class CitizenManager(BaseUserManager):
    def create_citizen(self, citizen_fname, citizen_email, citizen_phno, citizen_aadhar, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        citizen = self.model(citizen_fname=citizen_fname, citizen_email=citizen_email,
                             citizen_phno=citizen_phno, citizen_aadhar=citizen_aadhar, **extra_fields)
        citizen.set_password(extra_fields.get('password'))
        citizen.save(using=self._db)
        return citizen

    def create_superuser(self, citizen_fname, citizen_email, citizen_phno, citizen_aadhar, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_citizen(citizen_fname, citizen_email, citizen_phno, citizen_aadhar,
                                   password=password, **extra_fields)
