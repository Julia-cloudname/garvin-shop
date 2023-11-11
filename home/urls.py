from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('special_offers/', views.special_offers, name='special_offers'),
    
]
