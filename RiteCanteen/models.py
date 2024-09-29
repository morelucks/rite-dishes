from email.mime import image
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
import os

    
    
def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.FoodSecondPage_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.FoodSecondPage_id, ext)
    return os.path.join(upload_to, filename)





class Continental(models.Model):
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
    post2 = models.ForeignKey(Continental, on_delete= models.CASCADE, related_name= 'comments')
    def __str__(self):
        return self.body
    






class Fruit(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title
    




class Pastrils(models.Model):
    image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
    title = models.CharField(max_length = 200, null=True)
    body2 = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(null=True)
    writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    created_on = models.DateTimeField(auto_now = True, null=True)
    def __str__(self):
        return self.title


# class Drunk(models.Model):
#     image = models.ImageField(upload_to = 'images_uploaded', null=True, blank=True)
#     title = models.CharField(max_length = 200, null=True)
#     body2 = models.TextField(max_length=500, null=True, blank=True)
#     slug = models.SlugField(null=True)
#     writer = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
#     created_on = models.DateTimeField(auto_now = True, null=True)
#     def __str__(self):
#         return self.title


    


