from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.urls import reverse
from django.db.models import Max

from .models import Flight, Airport, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    # Get max index on flights data base
    max_id = Flight.objects.all().aggregate(Max('id'))['id__max']

    if flight_id <= max_id:
        flight = Flight.objects.get(pk=flight_id)   # pk = primary key
        return render(request, "flights/flight.html", {
            "flight": flight,
            "passengers": flight.passengers.all(),
            "non_passengers": Passenger.objects.exclude(flights=flight).all()
        })
    else:
        raise Http404()

def book(request, flight_id):

    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))