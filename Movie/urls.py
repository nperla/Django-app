from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieListCreate.as_view(), name='movie-list-create'),
    path('movies//', views.MovieRetrieveUpdateDestroy.as_view(), name='movie-retrieve-update-destroy'),
]
