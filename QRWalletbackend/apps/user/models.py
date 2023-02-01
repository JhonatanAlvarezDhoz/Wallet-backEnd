from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField 

# Create your models here.

class User(AbstractUser):

    phone = PhoneNumberField(null=True, blank=True)
    is_subscribe = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

        def __str__(self):
            return f"{self.username} {self.email}"

    