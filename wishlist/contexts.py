from django.shortcuts import get_object_or_404
from products.models import Product


def wishlist_contents(request):
    wishlist_items = []
    if request.user.is_authenticated:
        wishlist_items = Product.objects.filter(users_wishlist=request.user)
    
    context = {
        'wishlist_items': wishlist_items,
    }

    return context