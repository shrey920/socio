from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,related_name="message_sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,related_name="message_receiver")
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True, db_index=True)
