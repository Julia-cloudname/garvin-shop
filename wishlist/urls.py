from django.urls import path
from . import views

urlpatterns = [
    #wishlist
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add_to_wishlist/<int:product_id>', views.add_to_wishlist, name='user_wishlist'),
]