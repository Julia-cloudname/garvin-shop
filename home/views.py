from django.shortcuts import render
from products.models import Product, Review

def index(request):
    """ A view to return the index page """

    latest_reviews = Review.objects.order_by('-created_at')[:4]
    return render(request, 'home/index.html', {'latest_reviews': latest_reviews})
