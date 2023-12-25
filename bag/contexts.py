from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def calculate_price_based_on_quantity(quantity, base_price):
    """
    Applies a discount depending on quantity.
    """
    discount = Decimal(0)
    if 1 <= quantity < 10:
        discount = Decimal(0)
    elif 10 <= quantity < 60:
        discount = base_price * Decimal(0.25) 
    elif 60 <= quantity < 180:
        discount = base_price * Decimal(0.36)
    elif 180 <= quantity < 300:
        discount = base_price * Decimal(0.52)
    else:
        discount = base_price * Decimal(0.57)

    adjusted_price = base_price - discount

    return Decimal(round(float(adjusted_price)))

def bag_contents(request):
    """
    Calculates total cost and counts items based on their adjusted prices.
    """
    bag_items = []
    grand_total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        adjusted_price = calculate_price_based_on_quantity(quantity, product.price)
        
        grand_total += quantity * adjusted_price
        product_count += quantity
        
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'adjusted_price': adjusted_price,
            'base_price': product.price,
        })
    
    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
