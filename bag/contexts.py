from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def calculate_price_based_on_quantity(quantity):
    if 0 <= quantity <= 9:
        return 47
    elif 10 <= quantity <= 59:
        return 35
    elif 60 <= quantity <= 179:
        return 30
    elif 180 <= quantity <= 299:
        return 23
    else:
        return 20

def bag_contents(request):

    bag_items = []
    grand_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        
        adjusted_price = calculate_price_based_on_quantity(quantity)
        
        grand_total += quantity * adjusted_price
        product_count += quantity
        
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'adjusted_price': adjusted_price,
        })
    
    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
