from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('fun/',views.fun,name='fun')

]