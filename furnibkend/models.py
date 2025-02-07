from django.db import models # type: ignore

# Create your models here.
class furnitures(models.Model):
    name = models.CharField(max_length= 100) 
    img = models.ImageField(upload_to= 'images')
    desc = models.TextField() 
    price = models.IntegerField()
