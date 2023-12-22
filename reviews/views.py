from django.shortcuts import render
from reviews.models import Review
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404
from reviews.forms import ReviewForm 

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.product = product
            review.user = request.user
            review.user_rating = request.POST.get('user_rating', 0)
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'form': review_form,
    }

    return render(request, 'product_detail.html', context)
