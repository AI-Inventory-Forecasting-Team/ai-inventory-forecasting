from django.contrib.auth.models import AbstractUser
from django.db import models
from config.settings import AUTH_USER_MODEL as User

class CustomUser(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username