from email.mime import image
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os





class Drink(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    Commenter = models.CharField(max_length= 50)
    body = models.TextField()
    rites5 = models.ForeignKey(Drink, on_delete= models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body