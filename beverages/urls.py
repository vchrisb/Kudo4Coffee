from django.urls import path

from . import views

urlpatterns = [
    path('', views.beverage, name='beverage'),
]