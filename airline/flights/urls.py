from django.urls import path

from . import views

urlpatterns = [
    # default route/ index view
    path("", views.index, name="index"),
    # path for an individual flight via the flight id
    path("<int:flight_id>", views.flight, name="flight"),
    # path to book a flight via flight_id/book
    path("<int:flight_id>/book", views.book, name="book")
]
