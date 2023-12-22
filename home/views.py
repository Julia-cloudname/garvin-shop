from django.shortcuts import render
from products.models import Product
from reviews.models import Review

def index(request):
    """ A view to return the index page """

    latest_reviews = Review.objects.order_by('-created_at')[:4]
    products = Product.objects.all()[:6] 
    return render(request, 'home/index.html', {'latest_reviews': latest_reviews, 'products': products})

def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')

def special_offers(request):
    """ A view to return the special offers page """
    return render(request, 'home/special_offers.html')

def my_custom_page_not_found_view(request, exception):
    return render(request, '404.html', {}, status=404)