from products.models import Product
from django.contrib.auth.decorators import login_required
from wishlist.models import Wishlist
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

def history(request):
    """ A view to return the history page """
    print(request.user)
    print(request.path)
    print(request.method)

    return render(request, 'history/history.html')