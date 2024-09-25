from django.db import models

# Create your models here.

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('Topwear', 'Topwear'),
        ('Bottomwear', 'Bottomwear'),
        ('Footwear', 'Footwear'),
        ('Accessories', 'Accessories'),
    ]
    
    FASTENING_CHOICES = [
        ('Zipper', 'Zipper'),
        ('Velcro', 'Velcro'),
        ('Buttons', 'Buttons'),
        ('Magnetic', 'Magnetic'),
    ]

    PHYSICAL_CONDITION_CHOICES = [
        ('Mobility', 'Mobility impairment'),
        ('Sensory', 'Sensory sensitivity'),
        ('Prosthetics', 'Use of prosthetics'),
        ('Other', 'Other needs'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default='general')
    fastening_type = models.CharField(choices=FASTENING_CHOICES, max_length=50, default='button')
    physical_condition = models.CharField(choices=PHYSICAL_CONDITION_CHOICES, max_length=50, default='none')
    size = models.CharField(max_length=10, blank=True)
    material = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    image = models.ImageField(upload_to='clothing_items/', null=True, blank=True)


#class Order(models.Model):
 ### order_date = models.DateTimeField(auto_now_add=True)
    #delivery_address = models.TextField()
    
class Order(models.Model):
    name = models.CharField(max_length=100, default='default')
    email = models.EmailField(default='default@example.com')
    phone = models.CharField(max_length=15, default='+254794824427')
    address = models.TextField(default='default123')
    clothing_item = models.ForeignKey('ClothingItem', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default='1')
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} for {self.name}"