from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Add movies to the database'

    def handle(self, *args, **kwargs):
        json_file_path = 'movie/management/commands/movies_initial.json'


        
        with open(json_file_path) as file:
            movies = json.load(file)

        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                Movie.objects.create(title = movie['title'], 
                                      image = 'deafult.jpg',
                                     genre = movie['genre'], year = movie['year'])

                   