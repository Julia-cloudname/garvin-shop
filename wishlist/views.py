from django.shortcuts import render

def wishlist(request):
    """ A view that renders the wishlist contents page """
    return render(request, 'wishlist/wishlist.html')
