from platform import release
from pyexpat import model
from tkinter import CASCADE
from turtle import ondrag
from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    
    class Meta:
        db_table = 'actors'

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    running_time = models.IntegerField()
    actor = models.ManyToManyField(Actor, through="ActorMovie")

    class Meta:
        db_table = 'movies'

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        db_table = 'actors_movies'

