from django import forms
from products.models import Product
from reviews.models import Review

class ReviewForm(forms.ModelForm):
    """ Form for reviews """
    class Meta:
        model = Review
        fields = ['content'] 
        widgets = {
            'product': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            'created_at': forms.HiddenInput(),
            'user_rating': forms.HiddenInput(),
            'content': forms.Textarea
        }
        labels = {
            'content': 'Your Review',            
        }