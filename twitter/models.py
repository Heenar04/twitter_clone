from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Tweetclone(models.Model):
    class Meta(object):
        db_table = 'tweetclone'
    name = models.CharField(max_length=14)
    body = models.TextField(max_length=140)
    image = CloudinaryField('image', blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)   
