from django.shortcuts import render, get_object_or_404, redirect
from .models import ClothingItem
from .forms import OrderForm, ClothingFilterForm
from .utils import send_sms_notification
from .models import Order

# View to list clothing items
def clothing_list(request):
    clothing_items = ClothingItem.objects.all()
    return render(request, 'clothing_store/clothing_list.html', {'clothing_items': clothing_items})

# View to place an order
def place_order(request, item_id):
    item = get_object_or_404(ClothingItem, id=item_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        print("Form data:", request.POST)  # Check the form data received
        
        if form.is_valid():
            print("Form is valid")  # This line will confirm the form is valid
            order = form.save(commit=False)
            order.clothing_item = item
            order.save()  # Save the order to the database
            
            # Get the phone number from the form
            phone_number = form.cleaned_data.get('phone')
            print("Phone number from form:", phone_number)  # Print the phone number
            
            if not phone_number.startswith('+'):
                phone_number = f"+254{phone_number[-9:]}"
                print("Formatted phone number:", phone_number)  # Print the formatted phone number
            
            # Prepare SMS message
            message = f"Thank you for your order! Your order for {item.name} has been placed successfully."
            print("SMS message:", message)  # Print the SMS message
            
            # Send SMS notification
            sms_response = send_sms_notification(phone_number, message)
            print("SMS response:", sms_response)  # Print the response from the SMS API
            
            # Redirect to the order confirmation page
            return redirect('order_confirmation', item_id=item.id)
        else:
            print("Form errors:", form.errors)  # Print any form errors
    else:
        form = OrderForm(initial={'clothing_item': item})
    
    return render(request, 'clothing_store/place_order.html', {'form': form, 'item': item})

# View for the homepage
def homepage(request):
    return render(request, 'clothing_store/homepage.html')

def mission(request):
    return render(request, 'clothing_store/mission.html')

# View to browse clothing with filters
def browse_clothing(request):
    clothing_items = ClothingItem.objects.all()  # Initial queryset of all items
    form = ClothingFilterForm(request.GET or None)  # Get the form and populate it with GET params

    # Apply filters if the form is valid
    if form.is_valid():
        if form.cleaned_data.get('category'):
            clothing_items = clothing_items.filter(category=form.cleaned_data['category'])
        if form.cleaned_data.get('fastening_type'):
            clothing_items = clothing_items.filter(fastening_type=form.cleaned_data['fastening_type'])
        if form.cleaned_data.get('physical_condition'):
            clothing_items = clothing_items.filter(physical_condition=form.cleaned_data['physical_condition'])
        if form.cleaned_data.get('size'):
            clothing_items = clothing_items.filter(size=form.cleaned_data['size'])
        if form.cleaned_data.get('material'):
            clothing_items = clothing_items.filter(material=form.cleaned_data['material'])

    # Pass both the form and filtered items to the template
    context = {
        'clothing_items': clothing_items,
        'form': form,
    }
    return render(request, 'clothing_store/browse_clothing.html', context)
# View to show SMS updates page
def sms_updates(request):
    return render(request, 'clothing_store/sms_updates.html')

# Order delivery view
def OrderDeliveryView(View):
    def get(self, request):
        return render(request, 'clothing_store/order_delivery.html')

# Order confirmation view
def order_confirmation(request, item_id):
    item = ClothingItem.objects.get(id=item_id)
    return render(request, 'clothing_store/order_confirmation.html', {
        'item': item, 'order': Order})
