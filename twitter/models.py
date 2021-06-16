from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Tweetclone(models.Model):
    class Meta(object):
        db_table = 'tweetclone'
    name = models.CharField(max_length=14)
    body = models.TextField(max_length=140)
    image = CloudinaryField('image', blank= True, null= True)
    like_count=models.IntegerField('LikeCount',default=0,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)   


class Contact(models.Model):
    class Meta(object):
        db_table= 'contacts'
    name = models.CharField(max_length=14)
    email = models.EmailField(max_length=50, null=True, blank=True)
    body = models.TextField(max_length=140)
    