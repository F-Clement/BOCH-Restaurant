from . import views
from django.urls import path


urlpatterns = [
    path('', views.ReservationTable.as_view(),
         name='ReservationTable'),

]
