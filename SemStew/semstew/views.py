from django.shortcuts import render
from django.template import loader
from semstew.models import *


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
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/offer.html', context)


def delivery (request):

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


def about_us(request, language_id):
    about_us_headers = AboutUsConfig.objects.get(language=language_id)
    about_us_contents = AboutUs.objects.get(aboutus_config=about_us_headers.pk)
    context = {
        'about_us_headers': about_us_headers,
        'about_us_contents': about_us_contents
    }
    return render(request, 'semstew/aboutus.html', context)


def contact (request):
    template = loader.get_template('../templates/semstew/contact.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/semstew/contact.html', context)
