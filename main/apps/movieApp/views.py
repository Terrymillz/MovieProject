from django.shortcuts import render, redirect
from . import services
from .models import Watchlist
from ..User_app.models import User

# ===========================
# Template renders
# ===========================
def movie_page(request, id): # this renders the selected individual movie page
    in_list = False 
    if 'user' in request.session:
        user = User.objects.get(id=request.session['user'])
        watchlist = Watchlist.objects.filter(user__id=user.id)
        for movie in watchlist: #<-- this is to check if movie is already in watchlist
            if movie.api_Movie_code == id:
                in_list == True


    movie = services.get_movie(id)
    context = { #<-- info that goes to template
        'movie': movie['movie_info'],
        'cast': movie['cast_info'],
        'in_list': in_list
    }
    return render(request, 'movieApp/movie_page.html', context)

def cast_page(request, id): # this render the info page for the individual actor
    person_info = services.get_person(id)
    person = {
        'details': person_info['details'],
        'credits': person_info['credits']
    }
    return render(request, 'movieApp/cast_page.html', person )



# ===========================
#Post Routes
# ===========================

def add_to_watchlist(request, id): # the post route adds a movie to the Users watchlist
    if request.method == 'POST':
        movie = services.get_movie(id)
        data = {
            "movie": movie['movie_info'], # this is the data for the current movie being displayed
            "user_id": request.session['user'] # the logged in user id from session
        }
        Watchlist.objects.add_movie(data) #add movie to Watchlist
        return redirect('/movie/' + id)
