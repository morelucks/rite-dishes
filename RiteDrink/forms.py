from django import forms
from .models import Comment
from .models import Drink
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





        

class CommentForm(forms.ModelForm):
    Commenter = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your name'
        }))
    body = forms.CharField(max_length=100, widget = forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Comment here', 'rows':3
    }))
    class Meta:
        model = Comment
        fields = ['Commenter', 'body']
        
