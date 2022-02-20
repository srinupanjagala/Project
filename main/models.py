from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    image = models.ImageField(upload_to='img')
    description = models.CharField(max_length=200, null=True)
    disc_price = models.IntegerField(null=True)


class Orders(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.IntegerField()
    item = models.ForeignKey(Products, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
