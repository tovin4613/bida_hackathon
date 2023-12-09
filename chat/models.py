from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)