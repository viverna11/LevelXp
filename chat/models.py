from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class ChatRoom(models.Model):
    room_name = models.CharField(max_length=100, blank=False, null=False, default='room')
    description = models.TextField(blank=True, null=True)
    room_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    member = models.ManyToManyField(User, related_name='member', blank=True)




class Message(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Message by {self.author.username} at {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
    

