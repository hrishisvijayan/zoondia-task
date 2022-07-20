from dataclasses import field
import django


from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ['status']


    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class':'form-controll col-12'}
        )
        self.fields['price'].widget.attrs.update(
            {'class':'form-controll col-12'}
        )
        self.fields['quantity'].widget.attrs.update(
            {'class':'form-controll col-12'}
        )
        self.fields['image'].widget.attrs.update(
            {'class':'form-controll col-12'}
        )