from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    STATUS = [('Enabled', 'Enabled'),
              ('Disabled', 'Disabled')]
    CATEGORY = []

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS, default='Enabled')
    
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.post
    





    