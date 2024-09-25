# clothing_store/forms.py
from django import forms
from .models import Order
from .models import ClothingItem

class ClothingFilterForm(forms.Form):
    category = forms.ChoiceField(choices=ClothingItem.CATEGORY_CHOICES, required=False, label="Category")
    fastening_type = forms.ChoiceField(choices=ClothingItem.FASTENING_CHOICES, required=False, label="Fastening Type")
    physical_condition = forms.ChoiceField(choices=ClothingItem.PHYSICAL_CONDITION_CHOICES, required=False, label="Special Needs")
    size = forms.CharField(max_length=10, required=False, label="Size")
    material = forms.CharField(max_length=100, required=False, label="Material")

class OrderForm(forms.ModelForm):
    phone = forms.CharField(max_length=15, help_text="Enter your phone number for SMS updates.")
    
    class Meta:
        model = Order
        fields = ['name', 'email', 'phone', 'address', 'quantity']
        widgets = {
            'clothing_item': forms.HiddenInput(),  
        }

