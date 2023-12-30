from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm
from wishlist.models import Wishlist
from reviews.models import Review  
from reviews.forms import ReviewForm 
from history.views import add_to_history

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    card_type = None
    active_category = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            active_category = categories[0].name if categories else 'all'
        else:
            active_category = 'all'

        if 'card_type' in request.GET:
            card_type = request.GET['card_type']
            if card_type in ['horizontal', 'vertical']:
                products = products.filter(card_type=card_type)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            direction = request.GET['direction'] if 'direction' in request.GET else ''

            if sortkey == 'rating':
                sortkey = '-rating' if direction == 'desc' else 'rating'
            elif sortkey == 'name':
                sortkey = '-lower_name' if direction == 'desc' else 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = '-category__name' if direction == 'desc' else 'category__name'

            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'all_categories': Category.objects.all(),
        'active_category': active_category,
        'current_sorting': current_sorting,
        'current_card_type': card_type,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Display the details of a specific product, including reviews, ratings, 
    and wishlist status for authenticated users.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    review_form = ReviewForm()

    # Determine the formatted rating or set it to "No rating"
    formatted_rating = f"{product.rating:.1f}" if product.rating is not None else "No rating"

    # Check if the user is authenticated and add product to history
    if request.user.is_authenticated:
        wishlist_product_ids = Wishlist.objects.filter(user=request.user).values_list('product_id', flat=True)
        add_to_history(request, product_id)
    else:
        wishlist_product_ids = []

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
        'rating': formatted_rating,
        'wishlist_product_ids': wishlist_product_ids, 
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the shop """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))



