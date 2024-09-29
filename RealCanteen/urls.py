from django.urls import path
from . import views

app_name='RealCanteen'

urlpatterns = [

    path('FoodContinental2/', views.FoodContinental2, name='FoodContinental2'),
    path('<str:slug>', views.food2_detailView, name = 'food2_detail'),

]


