from django.urls import path
from food_menu import views

urlpatterns = [
    path('',views.index,name='index'),
]