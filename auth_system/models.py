from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CastomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='profile-avatar/', blank=True, null=True, default='static/img/default_avatar.png')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
