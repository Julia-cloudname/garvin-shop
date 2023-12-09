from django.contrib import admin
from .models import Product, ProductImage, Category, Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ['thumbnail_image', 'detailed_image']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'total_rating',
        'card_type',
    )

    ordering = ('sku',)

    inlines = [ProductImageInline]


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'content', 'created_at') 
    list_filter = ('product', 'user', 'created_at')
    search_fields = ('content', 'product__name', 'user__username')
    readonly_fields = ('created_at',)

admin.site.register(Review, ReviewAdmin)
