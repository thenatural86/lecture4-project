from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# display information about currently signed in user


def index(request):
    # if user is not authenticated, user attribute comes with request object
    if not request.user.is_authenticated:
        # redirect to login if not authenticated
        return HttpResponseRedirect(reverse("login"))
        # otherwise render user html
    return render(request, "users/user.html")


def login_view(request):
    # if the request method is post
    if request.method == "POST":
        # grab username and password from corresponding input fields
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate and login imported from django.contrib.auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # if authenticated successfully, login and redirected to index route which will render user.html
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            # otherwise redirect back to login page
            return render(request, "users/login.html", {
                # message passed in as context
                "message": "Invalid credentials."
            })
    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
