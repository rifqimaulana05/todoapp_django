from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('petugas', 'Petugas'),
        ('user', 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.TextField(blank=True)

    def __str__(self):
        return self.user.username