from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name