from django.contrib import admin
from .models import Product
from wishlist.models import Wishlist

class WishlistAdmin(admin.ModelAdmin):
    """ Admin for wishlists """
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'product', 'user')

admin.site.register(Wishlist, WishlistAdmin)
    
