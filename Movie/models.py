from django.db import models

# Create your models here.

class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'action'
        FANTASY = 'fantasy'
        ADVENTURE = 'adventure'
        ROMANCE = 'romance'
        SCI_FI = 'sci-fi'
        Anime = 'anime'

    title = models.CharField(max_length=100)
    producer = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=Genre.choices)
    release_date = models.DateField()

    def __str__(self):
        return self.title

