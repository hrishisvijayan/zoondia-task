
from django.db import models

# Create your models here.



class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.BooleanField(default=True)
    image= models.ImageField(upload_to = 'images/')

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    

