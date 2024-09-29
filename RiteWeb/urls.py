from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('coke/', views.coke, name = 'coke'),
    path('search/', views.searchR, name='searchR'),

    path('blog/<str:slug>', views.blog_detailView, name = 'blog_detail'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('About/', views.About, name='About'),
    path('EventPlan/', views.EventPlan, name='EventPlan'),
    path('EventWed/', views.EventWed, name='EventWed'),
    path('EventBirth/', views.EventBirth, name='EventBirth'),
    path('EventName/', views.EventName, name='EventName'),
    path('EventAnn/', views.EventAnn, name='EventAnn'),
    path('EventDiet/', views.EventDiet, name='EventDiet'),
    path('EventHot/', views.EventHot, name='EventHot'),
    path('EventCaf/', views.EventCaf, name='EventCaf'),
    path('EventRender/', views.EventRender, name='EventRender'),
    path('RitePhoto/', views.RitePhoto, name='RitePhoto'),
    path('StoreLocate/', views.StoreLocate, name='StoreLocate'),



]


