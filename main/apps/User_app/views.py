from django.shortcuts import render, redirect

from .models import User, Profile, Movie
from ..movieApp.models import Watchlist

from django.core.urlresolvers import reverse
"""
things that need to be added?
1. validation messages
2. make sure that password is protected using Bcrpt and confirm password

"""
# Create your views here.
# =================================================================
# template renders
# =================================================================
def login_page(request): #<--renders the login page template
    return render(request, 'User_app/login_page.html')

def register_page(request): #<--renders the register page template
    return render(request, 'User_app/register_page.html')




def profile(request): # <-- this renders the profile page
    if 'user' not in request.session:
        return redirect('/login')

    user = User.objects.get(id=request.session['user'])
    profile = Profile.objects.filter(user_id = User.objects.get(id = request.session['user'])) # this gets the profile information ascociated with User

    context = { # <-- information passed to template
    'profile' : profile,
    'user' : user,
    'watchlist': Watchlist.objects.filter(user=request.session["user"])
    }
    for movie in context['watchlist']:
        print movie.movie_title
    return render(request, "User_app/profile.html", context)

# =================================================================
# POST request's
# =================================================================
def register_account(request): #this function creates the account
    if request.method == 'POST':
        account_info = {
            "first_name": request.POST['first_name'],
            "last_name": request.POST['last_name'],
            "email": request.POST['email'],
            "password": request.POST['password']
        }
        result = User.objects.register(account_info)
        if result['errors'] == None:
            request.session['user'] = result['user'].id
            return redirect('/')
        else:
            print result['errors']
            return redirect("/register")


def log_user_in(request): # this is to the log the user in
    if request.method == 'POST':
        login_info = {
            "email": request.POST['email'],
            "password": request.POST['password']
        }

        result = User.objects.login(login_info)

        if result['errors'] == None:
            request.session['email'] = result['user'].email
            request.session['name'] = result['user'].first_name
            request.session['user'] = result['user'].id
            request.session['action'] = "logged in"
            return redirect('/')
        else:
            print result['errors']
            return redirect('/login')


def createProfile(request):
    if request.method == 'POST':
        profile = Profile.objects.create(
            birthday = request.POST['birthday'],
            hometown = request.POST['hometown'],
            country = request.POST['country'],
            user_id = User.objects.get(id = request.session['user'])
        )
    return redirect('/profile')


def logout(request):
    request.session.clear()
    return redirect('/')

























# end
