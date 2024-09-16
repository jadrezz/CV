from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class MyUser(AbstractUser):
    def get_absolute_url(self):
        return reverse('users:profile', kwargs={'username': self.username})
