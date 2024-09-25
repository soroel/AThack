from django.contrib import admin
from .models import ClothingItem
from .models import Order

# Register your models here.
admin.site.register(ClothingItem)
admin.site.register(Order)