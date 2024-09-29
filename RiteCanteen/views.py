from django.shortcuts import render
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from RiteWeb.forms import UserForm, UserProfileInfoForm
from django.views.generic import CreateView
# from .models import UserProfileInfo, Contact, AboutUs
from django.urls import reverse

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (TemplateView, DetailView, 
                                  ListView)
from .models import Continental, Fruit, Pastrils

# Create your views here.




def index2(request):
    return render(request,'base.html')

def FoodContinental(request):
    post2 = Continental.objects.all()
    return render(request, 'FoodContinental.html', {'posts': post2})

def food_detailView(request, slug):
    post2 = Continental.objects.get(slug = slug)
    comments = post2.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post2 = post2
            new_comment.save()
            return HttpResponseRedirect(reverse('RiteCanteen:food_detail', args = [str(post2.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'food_detail.html', {'posts': post2, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})
 


def FoodFruit(request):
    fish = Fruit.objects.all()
    return render(request, 'RiteCanteen/FoodFruit.html', {'fishs': fish})

def FoodPastrils(request):
    rites4 = Pastrils.objects.all()
    return render(request, 'RiteCanteen/FoodPastrils.html', {'rite': rites4})


