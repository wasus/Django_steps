from django.conf.urls import url, include
from django.contrib import admin
from about import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
