import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from movies.models import Actor,Movie,ActorMovie

class ActorView(View):
    def post(self, request):
        data = json.loads(request.body)
        Actor.objects.create(first_name=data['first_name'],
                             last_name=data['last_name'],
                             date_of_birth=data['date_of_birth']
        )
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)
    
    def get(self, request):
        actors = Actor.objects.all()
        result = []  
        for actor in actors:
            movie_list=[]
            movies = actor.movie_set.all()
            for movie in movies:
                movie_list.append(movie.title)
            result.append(
                {
                    "first_name" : actor.first_name,
                    "last_name" : actor.last_name,
                    "movie" : movie_list
                }
            )
        return JsonResponse({'results' : result}, status=200)
        
class MovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        Movie.objects.create(title=data['title'],
                             release_date=data['release_date'],
                             running_time=data['running_time']
        )
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)
    
    def get(self, request):
        movies = Movie.objects.all()
        result = []

        for movie in movies:
            actor_list=[]
            actors=movie.actor.all()
            for actor in actors:
                actor_list.append(actor.first_name)
            result.append(
                {
                    "title" : movie.title,
                    "running_time" : movie.running_time,
                    "actor" : actor_list
                }
            )
        return JsonResponse({'results' : result}, status=200)

class ActorMovieView(View):
    def post(self, request):
        data = json.loads(request.body)
        ActorMovie.objects.create(
            actor_id=data['actor_id'],
            movie_id=data['movie_id']
        )
        return JsonResponse({'MESSAGE' : 'SUCCESS'}, status=201)
    
        
