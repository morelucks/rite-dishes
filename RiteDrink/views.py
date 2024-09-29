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

# Create your views here.
from .models import Drink


def FoodDrink(request):
    rites5 = Drink.objects.all()
    return render(request, 'FoodDrink.html', {'rite': rites5})

def drink_detailView(request, slug):
    rites5 = Drink.objects.get(slug = slug)
    comments = rites5.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.rites5 = rites5
            new_comment.save()
            return HttpResponseRedirect(reverse('RiteDrink:drink_detail', args = [str(rites5.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'drink_detail.html', {'rite': rites5, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})
