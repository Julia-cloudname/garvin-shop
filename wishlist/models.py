from django.conf import settings
from django.db import models
from products.models import Product

class Wishlist(models.Model):
    """ Model to define the wishlist """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

    @property
    def current_rating(self):
        """ Returns the current rating of the product """
        return self.product.rating
