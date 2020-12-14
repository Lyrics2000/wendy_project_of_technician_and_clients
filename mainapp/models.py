from django.db import models
from django.db.models.query import ModelIterable
from django.db import models
import random
import os
from django.db.models import Q
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from mainapp.utils import unique_slug_generator,category_unique_slug_generator
from accounts.models import CustomUser

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance,filename):
    new_filename = random.randint(1,999992345677653234)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext = ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename = final_filename )


class TechnicianDetails(models.Model):
    TechnicianId = models.ManyToManyField(CustomUser)
    ShopLocation = models.CharField(max_length=200,blank=True,null=True)
    PhoneNumber = models.CharField(max_length=200,blank=True,null=True)
    Description = models.TextField(max_length=200,blank=True,null=True)
    
    def __str__(self):
        return str(self.TechnicianId)
    
    
    
class ProductTech(models.Model):
    TechnicianId = models.OneToOneField(TechnicianDetails,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_image = models.FileField(upload_to = upload_image_path ,null=True,blank=False)
    product_description = models.TextField()
    slug = models.SlugField(blank=True,unique=True)


    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={
            'slug': self.slug
        })
    
