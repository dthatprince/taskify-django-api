import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser



def validate_phone_number(value):
    # Regex pattern for a valid phone number (example for international format)
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_regex.match(value):
        raise ValidationError(_('Enter a valid phone number.'))

# Create your models here.
class User(AbstractUser):
    # custom fields
    full_name = models.CharField(max_length=55, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, unique=True, validators=[validate_phone_number])
    date_of_birth = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email' # or 'email' if you want to use email to log in
    REQUIRED_FIELDS = ['full_name', 'username', 'date_of_birth']





    