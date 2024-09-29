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
from .models import  Continental2

# Create your views here.





def FoodContinental2(request):
    rite = Continental2.objects.all()
    return render(request, 'FoodContinental2.html', {'rites': rite})

def food2_detailView(request, slug):
    rite = Continental2.objects.get(slug = slug)
    comments = rite.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.rite = rite
            new_comment.save()
            return HttpResponseRedirect(reverse('RealCanteen:food2_detail', args = [str(rite.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'food2_detail.html', {'rites': rite, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})
 