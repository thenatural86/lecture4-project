from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# import Flight and Passenger model from model.py
from .models import Flight, Passenger

# display a list of all flights


def index(request):
    return render(request, "flights/index.html", {
        # gets all of flights through Flight.object.all()
        "flights": Flight.objects.all()
    })

# view to render an individual flight, takes flight_id as arg


def flight(request, flight_id):
    # get the particular flight via the flight_id arg
    # use .get() and set the pk(primary key) to equal the flight_id
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        # pass flight as input to template
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
