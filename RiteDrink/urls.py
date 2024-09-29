from django.urls import path
from . import views

app_name='RiteDrink'

urlpatterns = [
    

    path('FoodDrink/', views.FoodDrink, name='FoodDrink'),
    path('<str:slug>', views.drink_detailView, name = 'drink_detail'),


]
