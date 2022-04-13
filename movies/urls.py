from django.urls import path

from movies.views import MovieView, ActorView, ActorMovieView

urlpatterns = [
    path('/movies', MovieView.as_view()),
    path('/actors', ActorView.as_view()),
    path('/actors_movies', ActorMovieView.as_view()),
    
]