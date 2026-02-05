from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    is_blocked = models.BooleanField(default=False)
    is_moderator = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

