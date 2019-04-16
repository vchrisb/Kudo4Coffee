from django.urls import path

from . import views

urlpatterns = [
    path('', views.beverage, name='beverage'),
    path('history', views.beverage_history, name='beverage_history'),
]