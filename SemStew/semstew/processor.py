from semstew.models import *


def show_menu(request):
    langs = Language.objects.all()
    branches = Branch.objects.all()
    return {'langs': langs,
            'branches': branches}
