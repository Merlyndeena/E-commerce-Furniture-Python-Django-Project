from django.db import models

# Create your models here.
class category_db(models.Model):
    C_Name=models.CharField(max_length=100,null=True,blank=True)
    C_Image=models.ImageField(upload_to="category_img",null=True,blank=True)
    C_Desc=models.TextField(max_length=100,null=True,blank=True)
class product_db(models.Model):
    cat_name=models.CharField(max_length=100,null=True,blank=True)
    p_name=models.CharField(max_length=100,null=True,blank=True)
    p_quan=models.IntegerField(null=True,blank=True)
    p_mrp=models.CharField(max_length=100,null=True,blank=True)
    p_desc=models.TextField(max_length=200,null=True,blank=True)
    p_coo=models.CharField(max_length=200,null=True,blank=True)
    p_manu=models.CharField(max_length=200,null=True,blank=True)
    p_img1=models.ImageField(upload_to="Items",null=True,blank=True)
    p_img2=models.ImageField(upload_to="Items",null=True,blank=True)
    p_img3=models.ImageField(upload_to="Items",null=True,blank=True)
