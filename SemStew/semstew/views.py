from django.http import HttpResponse
from django.template import loader

def index (request):
    template = loader.get_template('semstew/index.xhtml')
    context = {
        # Everything what is need from DB to HTML
    }
    return HttpResponse (template.render(context, request))