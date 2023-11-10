from django.db import models
from django.conf import settings


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='products/thumbnails/', null=True, blank=True)
    detailed_image = models.ImageField(upload_to='products/detailed/', null=True, blank=True)

    CARD_TYPES = (
        ('horizontal', 'Horizontal Card'),
        ('vertical', 'Vertical Card'),
    )
    card_type = models.CharField(
        max_length=10,
        choices=CARD_TYPES,
        default='vertical',
    )
    #wishlist
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="users_wishlist", blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    detailed_image = models.ImageField(upload_to='detailed/')

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user} on {self.product}'
