from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post_owner")
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='static/posts', null=True, blank=True)
    likes = models.ManyToManyField(User,related_name="post_likes")
