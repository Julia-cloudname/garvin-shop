from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Q, Avg

class Category(models.Model):
    """ Model to define the categories of products """
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ Model to define the products """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    thumbnail_image = models.ImageField(upload_to='products/thumbnails/', null=True, blank=True)
    detailed_image = models.ImageField(upload_to='products/detailed/', null=True, blank=True)
    rating = models.FloatField(
        null=True, 
        validators=[
            MinValueValidator(0.0),  
            MaxValueValidator(5.0)   
        ]
    )

    CARD_TYPES = (
        ('horizontal', 'Horizontal Card'),
        ('vertical', 'Vertical Card'),
    )
    card_type = models.CharField(
        max_length=10,
        choices=CARD_TYPES,
        default='vertical',
    )

    def update_rating(self):
        """ Method to update the average rating """
        reviews = self.reviews.all()
        average_rating = reviews.aggregate(Avg('user_rating'))['user_rating__avg']
        
        if average_rating is not None:
            self.rating = average_rating
        else:
            self.rating = None

        self.save()


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    """ Model to define the product images """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    thumbnail_image = models.ImageField(upload_to='thumbnails/')
    detailed_image = models.ImageField(upload_to='detailed/')

