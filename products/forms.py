
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'The title'}))
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                'Class': 'new-class-name two',
                'id': 'my-id',
                'rows': 10,
                'columns': 50
            }
            )
        )
    price = forms.DecimalField(initial=199.99)
    