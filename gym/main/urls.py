from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('calendar', views.calendar_view, name='calendar'),
    path('calendar/uprs', views.uprs, name='uprs'),
    path('ajax', views.uprs, name='uprs'),
]