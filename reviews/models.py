from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from django.db.models import Q, Avg

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=300) 
    created_at = models.DateTimeField(auto_now_add=True)
    user_rating = models.FloatField(
        default=0.0,
        validators=[
            MinValueValidator(0.0),  
            MaxValueValidator(5.0)   
        ]
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()

    def __str__(self):
        return f'Review by {self.user} on {self.product}'
    
