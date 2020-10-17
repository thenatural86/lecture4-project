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

# needs error checking for flight_id that does not exist


def flight(request, flight_id):
    # get the particular flight via the flight_id arg
    # use .get() and set the pk(primary key) to equal the flight_id
    flight = Flight.objects.get(pk=flight_id)

    return render(request, "flights/flight.html", {
        # pass flight as input to template
        "flight": flight,
        # can call passengers on flight b/c passengers is the 'related name' on the Passenger model
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

# takes flight_id as arg


def book(request, flight_id):
    # post method for manipulating information inside db
    if request.method == "POST":
        # get the flight whose pk is that flight_id
        flight = Flight.objects.get(pk=flight_id)
        # get the id of the passenger from request.POST["passenger"] (form with an input field whose name attribute is "passenger" )and convert to an int
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        # access a passengers flights via passenger.flight, then use the .add(flight) to add the flight
        passenger.flights.add(flight)
        # finally return a redirect to the flight page.
        # reverse takes the name of a view and gets what the actual url path should be. and as an arg to the flight route we pass in the flight.id structured as a tuple
        return HttpResponseRedirect(reverse("flight", args=(flight.id, )))
