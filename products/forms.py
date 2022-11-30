from django import forms
from django.forms import ModelForm
from .models import ProductCard, OrderItem, ShippingAddress, Order

class ProductCardForm(ModelForm):
    class Meta:
        model = ProductCard
        fields = ['product_image', 'title', 'description', 'price']

        labels = {
            'product_image': 'Product Image',
            'title': '',
            'description': '',
            'price': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the Product'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Add a short Description'}),
            'price': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Price'}),
        }

class UpdateQty(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']

        label = {
            'quantity': 'Quantity'
        }

        
class UpdateShoeSize(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['shoe_size']

        label = {
            'shoe_size': 'Size'
        }

        widgets = {
            'shoe_size': forms.CheckboxSelectMultiple(),
        }

class UpdateClothSize(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['cloth_size']

        label = {
            'cloth_size': 'Size'
        }

        widgets = {
            'cloth_size': forms.CheckboxSelectMultiple(),
        }

class AddShippingAddress(ModelForm):
    class Meta:
        model = ShippingAddress

        fields = ['address', 'country', 'postal_code', 'phone']

        label = {
            'postal_code': 'Postal Code'
        }

        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Address'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}),
            'postal_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Postal Code'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
        }

class CompleteOrder(ModelForm):
    class Meta:
        model = Order

        fields = ['compleated']
