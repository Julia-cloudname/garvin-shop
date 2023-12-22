from django.contrib import admin
from .models import Product, ProductImage, Category
from wishlist.models import Wishlist

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['thumbnail_image', 'detailed_image']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price',  'card_type', 'rating')
    ordering = ('sku',)
    inlines = [ProductImageInline]
    search_fields = ('sku', 'name', 'description', 'category__name')
    list_filter = ('category', 'card_type', 'rating')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    search_fields = ('name', 'friendly_name')



class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'product', 'user')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)