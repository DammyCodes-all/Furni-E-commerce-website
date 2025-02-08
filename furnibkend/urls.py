from django.urls import path,include
from . import views
urlpatterns = [
    path('' , views.index , name= 'index'),
    path('shop/', views.shop , name=  'shop'),
    path('about/', views.about , name= 'about'),
    path('register/',  views.register , name= 'register'),
]