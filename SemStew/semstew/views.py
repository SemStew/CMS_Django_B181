from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index (request):
    template = loader.get_template('../templates/index.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, '../templates/index.html', context)