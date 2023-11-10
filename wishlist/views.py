from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from checkout.models import Order
from products.models import Product

@login_required
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    print(products)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': products})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.error(request, f'Removed {product.name} from your Wishlist')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, f'Added {product.name} to your Wishlist')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])