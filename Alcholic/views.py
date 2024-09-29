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
from .models import  DrunkDrink

# Create your views here.



def FoodDrunk(request):
    tools = DrunkDrink.objects.all()
    return render(request, 'FoodDrunk.html', {'toy': tools})

def Drank_detailView(request, slug):
    tools = DrunkDrink.objects.get(slug = slug)
    comments = tools.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.tools = tools
            new_comment.save()
            return HttpResponseRedirect(reverse('Alcholic:Drank_detail', args = [str(tools.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'Drank_detail.html', {'toy': tools, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})

