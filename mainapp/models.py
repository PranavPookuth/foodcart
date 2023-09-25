from django.db import models

# Create your models here.
class cartdb(models.Model):
    productname=models.CharField(max_length=100,null=True,blank=True)
    username=models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True)
    totalprice = models.IntegerField(null=True,blank=True)
    image = models.ImageField(null=True)


class checkoutdb(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)

class userdb(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    password = models.IntegerField( null=True, blank=True)
    confirmpassword = models.IntegerField(null=True, blank=True)

