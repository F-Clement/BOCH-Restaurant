from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Reservation model for users can make reservations
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    number_of_people = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
