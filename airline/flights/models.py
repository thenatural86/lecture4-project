from django.db import models

# makemigrations - Look for any changes that have been made to models.py
# Then make a migration instruction for how to make those changes to the db

# migrate - applies changes to the db
# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    # returns a string representation of the object
    def __str__(self):
        # formatted string
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # foreign key that references another table (the airport table)
    # related_name - access relationship in the reverse order (Airport.departures)
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    # returns a string representation of the object

    def __str__(self):
        # formatted string
        # can access properties of object
        return f"{self.id}: {self.origin} to {self.destination}"


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(
        Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
