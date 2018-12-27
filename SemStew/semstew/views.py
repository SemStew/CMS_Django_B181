from django.shortcuts import render
from django.template import loader

def index (request):
    template = loader.get_template('../templates/semstew/index.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/index.html', context)

def branches (request):
    template = loader.get_template('../templates/semstew/branches.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/branches.html', context)

def offer (request):
    template = loader.get_template('../templates/semstew/offer.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/offer.html', context)

def delivery (request):
    template = loader.get_template('../templates/semstew/delivery.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/delivery.html', context)

def reservation (request):
    template = loader.get_template('../templates/semstew/reservation.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/reservation.html', context)

def aboutus (request):
    template = loader.get_template('../templates/semstew/aboutus.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/aboutus.html', context)

def contact (request):
    template = loader.get_template('../templates/semstew/contact.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/contact.html', context)
