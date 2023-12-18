from django.contrib import admin
from .models import Product, ProductImage, Category, Review
from wishlist.models import Wishlist


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['thumbnail_image', 'detailed_image']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'category', 'price', 'rating', 'card_type')
    ordering = ('sku',)
    inlines = [ProductImageInline]
    search_fields = ('sku', 'name', 'description', 'category__name')
    list_filter = ('category', 'rating', 'card_type')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')
    search_fields = ('name', 'friendly_name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'content', 'created_at') 
    list_filter = ('product', 'user', 'created_at')
    search_fields = ('content', 'product__name', 'user__username')
    readonly_fields = ('created_at',)


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at')
    search_fields = ('user__username', 'product__name')
    list_filter = ('created_at', 'product', 'user')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)