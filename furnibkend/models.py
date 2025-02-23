from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class furnitures(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images')
    desc = models.TextField()
    price = models.IntegerField()

class team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default='Member')
    image = models.ImageField(upload_to='images')
    desc = models.TextField()
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chair = models.ForeignKey(furnitures, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.chair.price

    def __str__(self):
        return f"{self.user.username} - {self.chair.name} ({self.quantity})"
# models.py
class ContactRequest(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"