from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductViewHistory
from products.models import Product
from django.utils import timezone
from django.contrib import messages

@login_required
def view_history(request):
    """
    Display the viewing history for the logged-in user.
    """
    user_history = ProductViewHistory.objects.filter(user=request.user)
    return render(request, 'history/history.html', {'history': user_history})

@login_required
def add_to_history(request, product_id):
    """
    Add a product view to the user's viewing history or update the timestamp if it already exists.
    """
    product = get_object_or_404(Product, pk=product_id)
    # Creates or updates the viewing history entry for the product
    history_entry, created = ProductViewHistory.objects.get_or_create(
        user=request.user, 
        product=product,
        defaults={'created_at': timezone.now()}
    )
    # Updates the viewing timestamp if the history entry already existed
    if not created:
        history_entry.created_at = timezone.now()
        history_entry.save()
    return redirect('product_detail', product_id=product.id)

@login_required
def remove_from_history(request, product_id):
    """
    Remove a product from the user's viewing history.
    """
    product = get_object_or_404(Product, pk=product_id)
    history_entry = ProductViewHistory.objects.get(
        user=request.user, 
        product=product
    )
    history_entry.delete()
    messages.success(request, f'{product.name} was removed from your viewing history')
    return redirect('view_history')