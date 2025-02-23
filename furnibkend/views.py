from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import furnitures,team, Cart,ContactRequest
from django.contrib import messages
from django.utils import timezone
# Create your views here.
def index(request):
    val = furnitures.objects.all()
    cart_items_count = 0
    random_items = val.order_by("?")[:3] # This will return 3 random items from
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    return render(request, 'index.html', {'random_items': random_items ,'cart_items_count': cart_items_count})
@login_required
def shop(request):
    val = furnitures.objects.all()
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    return render(request, 'shop.html', {'val': val ,'cart_items_count': cart_items_count})
@login_required
def about(request):
    team_member =team.objects.all()
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    return render(request, 'about.html', {'team_member': team_member ,'cart_items_count': cart_items_count})
@login_required
def blog(request):
    val = furnitures.objects.all()
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    return render(request, 'blog.html', {'val': val ,'cart_items_count': cart_items_count})
@login_required
def contact(request):
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    return render(request, 'contact.html', {'cart_items_count': cart_items_count })
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    total = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total ,'cart_items_count': cart_items_count})
@login_required
def services(request):
    val = furnitures.objects.all()
    if request.user.is_authenticated:
      cart_items_count= Cart.objects.filter(user=request.user).count()
    random_items = val.order_by("?")[:3] # This will return 3 random items from
    return render(request, 'services.html', {'random_items': random_items ,'cart_items_count': cart_items_count})
@login_required
def add_to_cart(request, chair_id):
        chair = get_object_or_404(furnitures, id=chair_id)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            chair=chair
        )
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        return redirect('/')
@login_required
def remove_from_cart(request, cart_id):
        cart_item = get_object_or_404(Cart, id=cart_id)
        cart_item.delete()
        return redirect('/cart')
def Send_contact(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if all([firstname, lastname, email, message]):
            try:
                contact = ContactRequest.objects.create(
                    firstname=firstname,
                    lastname=lastname,
                    email=email,
                    message=message
                )
                messages.success(request, 'Message sent successfully!')
            except Exception as e:
                messages.error(request, f'Error sending message: {str(e)}')
        else:
            messages.error(request, 'Please fill all fields')
        
        return redirect('contact')
        
    return render(request, 'contact.html')



