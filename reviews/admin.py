from django.contrib import admin
from products.models import Product
from reviews.models import Review

class ReviewAdmin(admin.ModelAdmin):
    """ Admin for reviews """
    list_display = ('product', 'user', 'content', 'created_at', 'user_rating') 
    list_filter = ('product', 'user', 'created_at')
    search_fields = ('content', 'product__name', 'user__username')
    readonly_fields = ('created_at',)

admin.site.register(Review, ReviewAdmin)
