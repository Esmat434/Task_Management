import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='accounts/')

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name='CustomUser'
        verbose_name_plural='CustomUsers'

class PasswordResetToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='password_reset')
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    created_at = models.DateField(auto_now_add=True)