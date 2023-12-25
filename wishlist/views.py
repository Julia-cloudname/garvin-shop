from products.models import Product
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required
def wishlist(request):
    """
    Display the wishlist of the logged-in user. Fetches and shows all wishlist items associated with the user.
    """
    wishlist_items = Wishlist.objects.filter(user=request.user)
    wishlist_product_ids = wishlist_items.values_list('product_id', flat=True)

    template = 'wishlist/wishlist.html'
    return render(request, template, {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist. Does nothing if the product is already in the wishlist.
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f'Added {product.name} to your Wishlist')
    else:
        messages.info(request, f'{product.name} is already in your Wishlist')
    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist. Redirects to the product detail page if the request came from there,
    otherwise redirects to the wishlist page.
    """
    product = get_object_or_404(Product, pk=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    if wishlist_item.exists():
        wishlist_item.delete()
        messages.success(request, f'{product.name} has been removed from your Wishlist.')
    else:
        messages.info(request, f'{product.name} was not in your Wishlist.')

    referer_url = request.META.get("HTTP_REFERER")
    if referer_url and reverse('product_detail', args=[product.id]) in referer_url:
        return redirect('product_detail', product_id=product.id)
    else:
        return redirect('wishlist')





