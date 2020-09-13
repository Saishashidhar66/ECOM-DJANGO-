from django.db import models
from django import forms
from ckeditor.fields import RichTextField

#Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null = True)
    phone = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.name
    
class Category(models.Model):
    c_name=models.CharField(max_length=20,null=True)
    
    def __str__(self):
        return self.c_name
    


class Product(models.Model):
    sizes = (
    ('s', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL')
    )

    name = models.CharField(max_length = 50, null = True)

    image = models.ImageField(upload_to = 'images', null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    description = RichTextField(null = True)
    color = models.CharField(max_length=10, null=True)
    size = models. CharField(max_length=20,choices=sizes, null=True)
    quantity = models.IntegerField(null = True)
    prize = models.FloatField(max_length=10, null=True)
    
    def __str__(self):
        return self.name

