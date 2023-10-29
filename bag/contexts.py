from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def calculate_price_based_on_quantity(quantity, base_price):
    discount = Decimal(0)   # Задаем начальное значение discount как Decimal
    if 0 <= quantity <= 9:
        discount = Decimal(0)
    elif 10 <= quantity <= 59:
        discount = base_price * Decimal(0.25)   # Преобразуем 0.25 в Decimal
    elif 60 <= quantity <= 179:
        discount = base_price * Decimal(0.36)   # Преобразуем 0.35 в Decimal
    elif 180 <= quantity <= 299:
        discount = base_price * Decimal(0.52)   # Преобразуем 0.45 в Decimal
    else:
        discount = base_price * Decimal(0.57)   # Преобразуем 0.50 в Decimal

    adjusted_price = base_price - discount
    adjusted_price = Decimal(round(float(adjusted_price)))

    return adjusted_price

def bag_contents(request):
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
