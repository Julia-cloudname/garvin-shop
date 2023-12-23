from django.db import models
from django.conf import settings
from products.models import Product

class ProductViewHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Product View Histories'

    def __str__(self):
        return f'{self.user.username} viewed {self.product.name}'
