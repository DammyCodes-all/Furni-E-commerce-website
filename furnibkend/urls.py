from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.index , name= 'index'),
    path('shop/', views.shop , name=  'shop'),
    path('about/', views.about , name= 'about'),
    path('services/' , views.services , name= 'services'),
    path('blog/', views.blog , name= 'blog'),
    path('contact/', views.contact , name= 'contact'),
    path('cart/', views.cart , name= 'cart'),
    path('Send_contact/', views.Send_contact , name= 'Send_contact'),
    path('add_to_cart/<int:chair_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]