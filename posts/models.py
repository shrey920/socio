from django.db import models
from django.conf import settings
from groups.models import *
User=settings.AUTH_USER_MODEL

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="post_owner")
    group = models.ForeignKey(Group,on_delete=models.PROTECT,null=True)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='static/posts', null=True, blank=True)
    likes = models.ManyToManyField(User,related_name="post_likes")
    date = models.DateTimeField(auto_now=True, db_index=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name="comment_post")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_owner")
    text = models.CharField(max_length=100)