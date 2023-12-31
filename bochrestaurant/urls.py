"""bochrestaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include('restaurant.urls'), name='restaurant_urls'),
    path('', views.index, name='index'),
    path('add_reservation/', views.add, name='add_reservation'),
    path('edit/<reservation_id>', views.edit, name='edit_reservation'),
    path('delete/<reservation_id>', views.delete, name='delete_reservation'),
    path('accounts/', include('allauth.urls')),



]
