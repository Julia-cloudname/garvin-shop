from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    thumbnail_image = forms.ImageField(label='Image Small', required=False, widget=CustomClearableFileInput)
    detailed_image = forms.ImageField(label='Image Detailed', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
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

