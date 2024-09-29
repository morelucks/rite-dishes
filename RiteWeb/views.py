from django.shortcuts import render, redirect
from .models import Food
from .forms import CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from RiteWeb.forms import UserForm, UserProfileInfoForm
from django.views.generic import CreateView
from .models import UserProfileInfo, Contact, AboutUs, EPLANNING, EWEDDING, EBIRTHDAY,  ENAMING, EANNIVERSARY, EDIETING, EHOTEL, ECAFETERIA, ERENDERING, RiteGallery, Location
from django.urls import reverse

from RiteDrink.models import Drink
from RealCanteen.models import Continental2
from RiteCanteen.models import Continental, Pastrils, Fruit
from Alcholic.models import DrunkDrink
from itertools import chain


# Create your views here.

def index(request):
    return render(request,'welcomepage.html')

def coke(request):
    post = Food.objects.all()
    return render(request,'coke.html', {'posts': post})



def blog_detailView(request, slug):
    post = Food.objects.get(slug = slug)
    comments = post.comments.all()
    new_comment = None
      
    if request.method == 'POST':
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args = [str(post.slug)]))
    else: 
        form = CommentForm()
    
    return render(request, 'blog_detail.html', {'post': post, 'form': form,
                                                'comments': comments, 
                                                'new_comment':new_comment})

    
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('coke'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
        
    else:
        return render(request, 'blogapp/login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('coke'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('coke')

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'blogapp/register.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})

class HomeView(TemplateView):
    template_name = 'blogapp/coke.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Admin = UserProfileInfo.objects.filter(user_type='Admin')
        context['Admin'] = Admin
        return context

class ContactView(CreateView):
    model = Contact
    fields = '__all__'
    template_name = 'blogapp/contact.html'


def About(request):
    bodys = AboutUs.objects.all()
    return render(request,'blogapp/About.html', {'body': bodys})


def StoreLocate(request):
    bodys34 = Location.objects.all()
    return render(request,'blogapp/StoreLocate.html', {'body': bodys34})



def EventPlan(request): 
    bodys2 = EPLANNING.objects.all()
    return render(request,'blogapp/EventPlan.html', {'body': bodys2})

def EventWed(request):
    bodys3 = EWEDDING.objects.all()
    return render(request,'blogapp/EventWed.html', {'body': bodys3})

def EventBirth(request):
    bodys4 = EBIRTHDAY.objects.all()
    return render(request,'blogapp/EventBirth.html', {'body': bodys4})

def EventName(request):
    bodys5 = ENAMING.objects.all()
    return render(request,'blogapp/EventName.html', {'body': bodys5})

def EventAnn(request):
    bodys6 = EANNIVERSARY.objects.all()
    return render(request,'blogapp/EventAnn.html', {'body': bodys6})

def EventDiet(request):
    bodys7 = EDIETING.objects.all()
    return render(request,'blogapp/EventDiet.html', {'body': bodys7})

def EventHot(request):
    bodys8 = EHOTEL.objects.all()
    return render(request,'blogapp/EventHot.html', {'body': bodys8})

def EventCaf(request):
    bodys9 = ECAFETERIA.objects.all()
    return render(request,'blogapp/EventCaf.html', {'body': bodys9})

def EventRender(request):
    bodys1 = ERENDERING.objects.all()
    return render(request,'blogapp/EventRender.html', {'body': bodys1})

def RitePhoto(request):
    photos1 = RiteGallery.objects.all()
    return render(request,'blogapp/RitePhoto.html', {'photo': photos1})


def searchR(request):
    results = None   # Initialize results to None

    if 'keyword' in request.GET:
        keyword = request.GET['keyword'].strip().lower()

        #print(f"Search Keyword: {keyword}")  

        result1 = Drink.objects.filter(title__icontains=keyword)
        result2 = Continental2.objects.filter(title__icontains=keyword)
        result3 = Continental.objects.filter(title__icontains=keyword)
        result4 = DrunkDrink.objects.filter(title__icontains=keyword)
        result5 = Fruit.objects.filter(title__icontains=keyword)
        result6 = Pastrils.objects.filter(title__icontains=keyword)

        results = chain( result1, result2, result3, result4, result5, result6)

        #print(f"Results: {results}")  # Debugging line

    context = {
        'results': results,
    }

    return render(request, 'blogapp/search.html', context)
