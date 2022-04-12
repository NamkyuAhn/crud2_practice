from pyexpat import model
from tkinter import CASCADE
from turtle import ondrag
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=300, null=False)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE) 
    name = models.CharField(max_length=45,null=False)
    age = models.IntegerField(null=False)

    class Meta:
        db_table = 'dogs'

