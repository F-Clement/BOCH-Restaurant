from django.contrib import admin
from .models import Reservation

# Register Reservation model

# admin.site.register(Reservation)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time')
