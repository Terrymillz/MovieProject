from __future__ import unicode_literals
from ..User_app.models import User
from django.db import models

# Create your models here.
class WatchlistManager(models.Manager):
    def add_movie(self, data):
        user = User.objects.get(id=data['user_id'])
        movie = data['movie']
        print movie['poster_path']
#=============================================================================
        # might need to add function to make sure the same movie cannont be added twice
#=============================================================================
        Watchlist.objects.create(
            api_Movie_code = movie['id'],
            movie_title = movie['title'],
            poster_path = movie['poster_path'],
            user = user
        )
        return



class Watchlist(models.Model): #creates a watchlist
    api_Movie_code = models.CharField(max_length=100)
    movie_title = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = WatchlistManager()
