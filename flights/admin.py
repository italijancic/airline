from django.contrib import admin

from .models import Flight, Airport, Passenger

# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    list_display = ('code', 'city')

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    list_display = ("first", "last", "created_on")
    filter_horizontal = ("flights",)

admin.site.register(Airport, AirportAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)