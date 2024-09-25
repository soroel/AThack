# clothing_store/forms.py
from django import forms
from .models import Order
from .models import ClothingItem

class ClothingFilterForm(forms.ModelForm):
    class Meta:
        model = ClothingItem
        fields = ['category', 'fastening_type', 'physical_condition', 'size', 'material']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'fastening_type': forms.Select(attrs={'class': 'form-control'}),
            'physical_condition': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.Select(attrs={'class': 'form-control'}),
            'material': forms.Select(attrs={'class': 'form-control'}),
        }
class OrderForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, help_text="Enter your phone number for SMS updates.")
    
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'quantity']
        widgets = {
            'clothing_item': forms.HiddenInput(),  
        }

