from products.models import Product
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist_item.delete()
        message = f'{product.name} has been removed from your Wishlist'
    else:
        message = f'Added {product.name} to your Wishlist'
    messages.info(request, message)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    if wishlist_item.exists():
        wishlist_item.delete()
        product.delete()
        messages.success(request, f'{product.name} has been removed from your Wishlist.')
    else:
        messages.error(request, f'{product.name} is not in your Wishlist.')
    return redirect('wishlist')
