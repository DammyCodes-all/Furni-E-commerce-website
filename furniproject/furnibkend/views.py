from django.shortcuts import render
from .models import furnitures

# Create your views here.
def index (request):
    val1 = furnitures( )
    val1.name = 'Nordio chair'
    val1.price = 30
    val2 = furnitures()
    val2.name ='Ergonomic chair'
    val2.price = 40
    val3 = furnitures()
    val3.name = 'Sapa chair'
    val3.price = 10
    val = [val1 ,val2 , val3]
    return render ( request, 'index.html' , {'val': val} )
