from django.shortcuts import render
from django.views import generic
from .models import Reservation


# Create view for reservation model


class ReservationTable(generic.ListView):
    model = Reservation
    template_name = "reservation.html"


def index(request):
    return render(request, "../templates/index.html")
