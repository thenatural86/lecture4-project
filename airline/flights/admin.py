from django.contrib import admin
# import models
from .models import Flight, Airport, Passenger

# Register your models here.

# can configure the admin interface a particular way
# class FlightAdmin is subclass of ModelAdmin, can specify how the FlightAdmin page will be displayed. So we have access to the fields passed in as list_display


class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    # filter_horizontal lets you manipulate many to many relationships
    filter_horizontal = ("flights",)


# tells admin app that i want to use the admin app to manipulate these models
#
admin.site.register(Airport)
# use the FlightAdmin PassengerAdmin settings when we view the interface
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
