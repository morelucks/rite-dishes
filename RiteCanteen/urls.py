from django.urls import path
from . import views

app_name='RiteCanteen'

urlpatterns = [
    path('index2/', views.index2, name = 'index2'),
    path('FoodContinental/', views.FoodContinental, name='FoodContinental'),
    path('<str:slug>', views.food_detailView, name = 'food_detail'),
    path('FoodFruit/', views.FoodFruit, name='FoodFruit'),
    path('FoodPastrils/', views.FoodPastrils, name='FoodPastrils'), 
    

]

