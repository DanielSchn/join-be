from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    initials = models.CharField(max_length=2)
    color = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username