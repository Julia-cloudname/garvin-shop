from django.contrib import admin
from .models import ProductViewHistory

class HistoryAdmin(admin.ModelAdmin):
    """ Allows us to add and edit product view history in the admin. """
    list_display = ('product', 'user', 'created_at')
    ordering = ('created_at', 'user', 'product')
    search_fields = ('product__name', 'user__username')
    list_filter = ('product', 'user', 'created_at')

admin.site.register(ProductViewHistory, HistoryAdmin)
