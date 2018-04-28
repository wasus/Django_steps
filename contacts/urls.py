from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('contacts/', views.contacts, name='contacts'),
]
