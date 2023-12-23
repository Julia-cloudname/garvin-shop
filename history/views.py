from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductViewHistory
from products.models import Product

@login_required
def view_history(request):
    user_history = ProductViewHistory.objects.filter(user=request.user)
    return render(request, 'history/history.html', {'history': user_history})

@login_required
def add_to_history(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    ProductViewHistory.objects.create(user=request.user, product=product)
    return redirect('product_detail', product_id=product_id)
