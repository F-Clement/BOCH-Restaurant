from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .forms import ReservationForm
from django.views.generic.edit import FormView

from .models import Reservation


# Create view for reservation model


class ReservationTable(generic.ListView):
    model = Reservation
    template_name = "reservation.html"


def index(request):
    return render(request, "../templates/index.html")


def add(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    form = ReservationForm()
    context = {
        'form': form
    }

    return render(request, "../templates/add_reservation.html", context)


def edit(request, reservation_id):
    reserved = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reserved)
        if form.is_valid():
            form.save()
            return redirect('reservation')
    form = ReservationForm(instance=reserved)
    context = {
        'form': form
    }
    return render(request, "../templates/edit_reservation.html", context)

# def ReservationForm(request):

#     context = {}

#     return render(request, 'reservation.html', context)
