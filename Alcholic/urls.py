from django.urls import path
from . import views

app_name='Alcholic'

urlpatterns = [

    path('FoodDrunk/', views.FoodDrunk, name='FoodDrunk'), 
    path('<str:slug>', views.Drank_detailView, name = 'Drank_detail'),


]


