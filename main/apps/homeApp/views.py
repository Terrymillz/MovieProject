from django.shortcuts import render, redirect
from . import services
from ..User_app.models import User

# Create your views here.
"""
api key = 286abf6056d0a1338f772d1b7202e728
"""
def index(request):
    if "user" in request.session :
        status = 'You are logged in'

        user = User.objects.get(id=request.session['user'])
        name = user.first_name
    else:
        status = "You are NOT logged in"
        name = ""

    result = services.get_discover()
    return render(request, 'homeApp/index.html', {'status': status, 'result': result, "name": name})


def testing(request):
    return redirect('/')
