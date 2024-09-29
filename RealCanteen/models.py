from email.mime import image
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os



class Continental2(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 250, null=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField()
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    Commenter = models.CharField(max_length= 50)
    body = models.TextField()
    rite = models.ForeignKey(Continental2, on_delete= models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body