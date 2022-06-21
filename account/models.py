from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=150, null=True, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=150, null=True, blank=False, verbose_name="Last Name")
    username = models.CharField(max_length=200, null=True, default=None, unique=True, verbose_name="Username")
    email = models.EmailField(null=True, unique=True, verbose_name="Email Address")
    picture = models.ImageField(null=True, blank=True, verbose_name="Profile Picture")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return f'{self.email}'