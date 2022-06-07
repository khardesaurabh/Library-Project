"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('addbook/', views.addbook, name='addbook'),
    path('displaybooks/', views.displaybooks, name='displaybooks'),
    path('deletebook/<int:id>/', views.deletebook, name='deletebook'),
    path('updatebook/<int:id>/', views.updatebook, name='updatebook'),
    path('searchbook/', views.searchbook, name='searchbook'),
    path('displayusers/', views.displayusers, name='displayusers'),
    path('contact/', views.contact, name='contact'),
]