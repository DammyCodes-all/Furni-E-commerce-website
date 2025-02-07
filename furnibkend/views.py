from django.shortcuts import render
from .models import furnitures

# Create your views here.
def index (request):
    val = furnitures.objects.all()
    return render ( request, 'index.html' , {'val': val} )
