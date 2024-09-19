from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    username = models.CharField(max_length=30)
    first_name =None
    last_name =None
    email = models.EmailField(unique=True)
    last_login = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
