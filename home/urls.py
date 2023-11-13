from django.urls import path
from . import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('special_offers/', views.special_offers, name='special_offers'),
    
]

handler404 = 'home.views.my_custom_page_not_found_view'