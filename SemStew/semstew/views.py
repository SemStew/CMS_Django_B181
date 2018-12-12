from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index (request):
    template = loader.get_template('semstew/index.html')
    context = {
        # Everything what is need from DB to HTML
    }
    return render(request, 'semstew/index.html', context)