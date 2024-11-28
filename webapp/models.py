from django.db import models

# Create your models here.
class contactdb(models.Model):
    f_name=models.CharField(max_length=100,null=True,blank=True)
    l_name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    msg=models.TextField(max_length=100,null=True,blank=True)
class signup_db(models.Model):
    s_name=models.CharField(max_length=100,null=True,blank=True)
    s_email=models.CharField(max_length=100,null=True,blank=True)
    s_mob=models.CharField(max_length=100,null=True,blank=True)
    s_pass=models.CharField(max_length=100,null=True,blank=True)
    s_newpass=models.CharField(max_length=100,null=True,blank=True)
class cartdb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    prod_name=models.CharField(max_length=100,null=True,blank=True)
    quan=models.IntegerField(max_length=100,null=True,blank=True)
    price=models.IntegerField(max_length=100,null=True,blank=True)
    tprice=models.IntegerField(null=True,blank=True)
    cart_img=models.ImageField(upload_to="Cart_Images",null=True,blank=True)
class orderdb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    phn=models.CharField(max_length=100,null=True,blank=True)
    tprice=models.IntegerField(null=True,blank=True)
    desc=models.TextField(max_length=100,null=True,blank=True)



