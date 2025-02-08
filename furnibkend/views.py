from django.shortcuts import render
from .models import furnitures

# Create your views here.
def index(request):
    val = furnitures.objects.all()
    return render(request, 'index.html', {'val': val})

def shop(request):
    val = furnitures.objects.all()
    return render(request, 'shop.html', {'val': val})
def about(request):
    val = furnitures.objects.all()
    return render(request, 'about.html', {'val': val})
def blog(request):
    val = furnitures.objects.all()
    return render(request, 'blog.html', {'val': val})
def cart(request):
    val = furnitures.objects.all()
    return render(request, 'cart.html', {'val': val})
def services(request):
    val = furnitures.objects.all()
    return render(request, 'services.html', {'val': val})
